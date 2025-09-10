#!/data/data/com.termux/files/usr/bin/env python3.12
import sys
sys.path.insert(0, "/data/data/com.termux/files/usr/lib/python3.12/site-packages")

import argparse
from hakurafixlag.run_fix_lag import run_fix_lag

def main():
    parser = argparse.ArgumentParser(description="Fix lag, tối ưu hệ thống, gửi file telegram.")
    parser.add_argument('-n', '--now', action='store_true', help='Chạy tối ưu ngay')
    parser.add_argument('--dir', type=str, default='/storage/emulated/0/Download', help='Thư mục gửi file')
    args = parser.parse_args()

    if args.now:
        run_fix_lag(args.dir)

if __name__ == "__main__":
    main()
