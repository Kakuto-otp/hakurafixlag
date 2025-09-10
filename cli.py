import argparse
from hakurafixlag import run_fix_lag

def main():
    parser = argparse.ArgumentParser(description="Fix lag, tối ưu hệ thống, gửi file telegram.")
    parser.add_argument('-n', '--now', action='store_true', help='Chạy tối ưu ngay')
    parser.add_argument('--dir', type=str, default='/storage/emulated/0/Download', help='Thư mục gửi file')
    args = parser.parse_args()

    if args.now:
        run_fix_lag(args.dir)

if __name__ == "__main__":
    main()