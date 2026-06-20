#!/usr/bin/env python3
"""
Video Compressor - Reduce video file sizes locally
Requires: FFmpeg installed on your system
"""

import subprocess
import os
import sys
from pathlib import Path


def check_ffmpeg():
    """Check if FFmpeg is installed"""
    try:
        subprocess.run(['ffmpeg', '-version'],
                       capture_output=True,
                       check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ FFmpeg not found!")
        print("Install it:")
        print("  macOS: brew install ffmpeg")
        print("  Windows: choco install ffmpeg OR download from ffmpeg.org")
        print("  Ubuntu/Debian: sudo apt install ffmpeg")
        return False


def get_file_size(filepath):
    """Get file size in MB"""
    return os.path.getsize(filepath) / (1024 * 1024)


def compress_video(input_file, output_file, quality='medium', preset='medium'):
    """
    Compress a video file

    quality options:
      'low'    - smaller file, lower quality (CRF 28)
      'medium' - balanced (CRF 23)
      'high'   - better quality, larger file (CRF 18)

    preset options (speed vs compression):
      'fast'   - quicker encoding, larger file
      'medium' - balanced
      'slow'   - better compression, takes longer
    """

    # Quality settings (CRF: 0-51, lower = better quality, ~23 is default)
    quality_map = {
        'low': 28,
        'medium': 23,
        'high': 18
    }

    crf = quality_map.get(quality, 23)
    preset = preset.lower()

    if not os.path.exists(input_file):
        print(f"❌ File not found: {input_file}")
        return False

    original_size = get_file_size(input_file)

    print(f"📹 Starting compression...")
    print(f"   Input: {input_file}")
    print(f"   Original size: {original_size:.2f} MB")
    print(f"   Quality: {quality} | Preset: {preset}")
    print(f"   Output: {output_file}")
    print()

    try:
        command = [
            'ffmpeg',
            '-i', input_file,
            '-c:v', 'libx264',           # video codec
            '-crf', str(crf),             # quality (lower = better)
            '-preset', preset,            # encoding speed
            '-c:a', 'aac',               # audio codec
            '-b:a', '128k',              # audio bitrate
            '-y',                        # overwrite output without asking
            output_file
        ]

        subprocess.run(command, check=True)

        compressed_size = get_file_size(output_file)
        reduction = ((original_size - compressed_size) / original_size) * 100

        print(f"\n✅ Compression complete!")
        print(f"   Original:   {original_size:.2f} MB")
        print(f"   Compressed: {compressed_size:.2f} MB")
        print(f"   Reduction:  {reduction:.1f}%")

        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ Compression failed: {e}")
        return False


def batch_compress(folder_path, quality='medium', preset='medium'):
    """Compress all video files in a folder"""
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv']
    folder = Path(folder_path)

    if not folder.exists():
        print(f"❌ Folder not found: {folder_path}")
        return

    videos = [f for f in folder.iterdir()
              if f.suffix.lower() in video_extensions]

    if not videos:
        print(f"❌ No video files found in {folder_path}")
        return

    print(f"Found {len(videos)} video(s) to compress\n")

    for i, video in enumerate(videos, 1):
        output_file = video.parent / f"{video.stem}_compressed{video.suffix}"
        print(f"[{i}/{len(videos)}]")
        compress_video(str(video), str(output_file), quality, preset)
        print()


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print(
            "  python video_compressor.py <input_file> [output_file] [quality] [preset]")
        print("\nExamples:")
        print("  python video_compressor.py video.mp4")
        print("  python video_compressor.py video.mp4 compressed.mp4 low fast")
        print("  python video_compressor.py video.mp4 compressed.mp4 high slow")
        print("\nQuality: low | medium (default) | high")
        print("Preset:  fast | medium (default) | slow")
        print("\nTo compress all videos in a folder:")
        print(
            "  python video_compressor.py --batch /path/to/folder [quality] [preset]")
        return

    if not check_ffmpeg():
        sys.exit(1)

    # Batch mode
    if sys.argv[1] == '--batch':
        if len(sys.argv) < 3:
            print(
                "Usage: python video_compressor.py --batch /path/to/folder [quality] [preset]")
            return
        folder = sys.argv[2]
        quality = sys.argv[3] if len(sys.argv) > 3 else 'medium'
        preset = sys.argv[4] if len(sys.argv) > 4 else 'medium'
        batch_compress(folder, quality, preset)
        return

    # Single file mode
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else f"{Path(input_file).stem}_compressed{Path(input_file).suffix}"
    quality = sys.argv[3] if len(sys.argv) > 3 else 'medium'
    preset = sys.argv[4] if len(sys.argv) > 4 else 'medium'

    compress_video(input_file, output_file, quality, preset)


if __name__ == '__main__':
    main()
