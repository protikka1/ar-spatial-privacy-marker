"""ASPM optical marker detection prototype (OpenCV required).

Detects a printed reference marker in camera frames using ORB features and
homography. It does NOT disable scanning, protect a location by itself, or
establish legal restrictions. Applications must enforce the opt-out policy.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import cv2


def detect_marker(reference, frame, *, min_matches=18, min_inliers=12):
    """Return detection details or None for an image with no robust marker match."""
    if reference is None or frame is None:
        raise ValueError("Both reference and frame images are required")
    gray_ref = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY) if reference.ndim == 3 else reference
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) if frame.ndim == 3 else frame
    orb = cv2.ORB_create(nfeatures=1600)
    key_ref, des_ref = orb.detectAndCompute(gray_ref, None)
    key_frame, des_frame = orb.detectAndCompute(gray_frame, None)
    if des_ref is None or des_frame is None or len(key_ref) < 4 or len(key_frame) < 4:
        return None
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
    pairs = matcher.knnMatch(des_ref, des_frame, k=2)
    good = [a for pair in pairs if len(pair) == 2 for a, b in [pair] if a.distance < 0.72 * b.distance]
    if len(good) < min_matches:
        return None
    import numpy as np
    src = np.float32([key_ref[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst = np.float32([key_frame[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    matrix, mask = cv2.findHomography(src, dst, cv2.RANSAC, 4.0)
    if matrix is None or mask is None or int(mask.sum()) < min_inliers:
        return None
    h, w = gray_ref.shape[:2]
    corners = np.float32([[0, 0], [w, 0], [w, h], [0, h]]).reshape(-1, 1, 2)
    polygon = cv2.perspectiveTransform(corners, matrix).reshape(4, 2)
    return {"marker_id": "ASPM-V1-OPT-OUT", "matches": len(good),
            "inliers": int(mask.sum()), "corners": polygon.tolist()}


def main():
    p = argparse.ArgumentParser(description="Detect an ASPM marker in a still image")
    p.add_argument("--reference", required=True, help="Raster PNG/JPG of SVG marker")
    p.add_argument("--image", required=True, help="Photo containing the printed marker")
    args = p.parse_args()
    reference = cv2.imread(str(Path(args.reference)))
    image = cv2.imread(str(Path(args.image)))
    if reference is None or image is None:
        p.error("Unable to read reference or input image")
    import json
    print(json.dumps({"detected": (result := detect_marker(reference, image)) is not None,
                      "result": result}, indent=2))
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
