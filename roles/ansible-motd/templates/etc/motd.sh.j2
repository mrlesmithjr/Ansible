#!/usr/bin/env bash

## Colors for script ##

black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[1;33m"
blue="\033[0;34m"
light_purple="\033[1;35m"
cyan="\033[0;36m"
white="\033[1;37m"

reset="\033[0m"

## Colors for script - End ##


# current date
date="$(date)"

# Current CPU Load
cpu_load="$(cat /proc/loadavg | awk '{print $1*100 "%"}')"

# Current CPU Usage
cpu_usage="$(top -b -n1 | grep 'Cpu(s)')"

# Disk mounts
disk_mounts="$(df -hT | grep -Ev 'devtmpfs|tmpfs')"

# used disk space
disk_usage="$(df -h | awk '{if($(NF) == "/") {print $(NF-1); exit;}}')"

# Measure DNS response time
if type dig > /dev/null 2>&1; then
  dns_response="$(dig google.com | grep 'Query time:' | awk '{print $4,$5}')"
else
  dns_response="dig command not found, please install"
fi

# Capture DNS Servers
dns_servers="$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}' | tr '\r\n' ' ')"

# Capture Interfaces
interfaces="$(ip link show | awk -F: '$1>0 {print $2}' | grep -v lo)"

# Using captured interfaces loop through them and capture:
# link state and ip address
# Only if IP address is defined
ips="$(for int in ${interfaces[@]};
  do
    state="$(ip link show $int | awk '{print $9}')"
    ip_addr="$(ip -4 add show $int | grep inet | awk '{print $2}'| awk -F/ '{print $1}')"
    if [ ! -z $ip_addr ]; then
      echo "[$int/$state]:" $ip_addr
    fi
  done
)"

# Buffer/Cache memory
memory_buffer_cache="$(free -m | awk '($1=="Mem:"){memBufferCache=$6} END{printf "%.0fM", memBufferCache}')"

# Free memory
memory_free="$(free -m | awk '($1=="Mem:"){memFree=$4} END{printf "%.0fM", memFree}')"

# Total memory
memory_total="$(free -m | awk '($1=="Mem:"){memTotal=$2} END{printf "%.0fM", memTotal}')"

# used memory
memory_usage="$(free -m | awk '($1=="Mem:"){memTotal=$2} {memUsed=$3} END{printf "%.1f%%", memUsed/memTotal * 100}')"

# Detect OS
if [ -f /etc/lsb-release ]; then
  os=$(lsb_release -s -d)
  elif [ -f /etc/debian_version ]; then
  os="Debian $(cat /etc/debian_version)"
  elif [ -f /etc/redhat-release ]; then
  os=`cat /etc/redhat-release`
else
  os="$(uname -s) $(uname -r)"
fi

# used swap memory
swap_usage="$(free -m | awk '($1=="Swap:"){swapTotal=$2; swapUsed=$3} END{printf "%.1f%%", swapUsed/swapTotal * 100}')"

# Capture top 5 processes by cpu
top_processes_cpu="$(ps aux k-pcpu | head -6)"

printf "${green}System Information for $HOSTNAME on ${date}\n"
printf "================================================================================\n"

printf "${white}OS                    :${cyan} %s\n" "${os}"
printf "\n"
printf "${white}CPU Load              :${cyan} %s\n" "${cpu_load}"
printf "${white}CPU Usage             :\n"
printf "${cyan}%s\n" "${cpu_usage}"
printf "\n"
printf "${white}Top 5 Processes(CPU)  :\n"
printf "${cyan}%s\n" "${top_processes_cpu}"
printf "\n"
printf "${white}Memory Total          :${cyan} %s\n" "${memory_total}"
printf "${white}Memory Free           :${cyan} %s\n" "${memory_free}"
printf "${white}Memory Buffer/Cache   :${cyan} %s\n" "${memory_buffer_cache}"
printf "${white}Memory Usage          :${cyan} %s\n" "${memory_usage}"
printf "${white}Swap Usage            :${cyan} %s\n" "${swap_usage}"
printf "\n"
# printf "${white}Total Disk Usage      :${cyan} %s\n" "${disk_usage}"
printf "${white}Disk Mounts           :\n"
printf "${cyan}%s\n" "${disk_mounts}"
printf "\n"
printf "${white}IP Addresses          :\n"
printf "${cyan}%s\n" "${ips}"
printf "\n"
printf "${white}DNS Servers           :${cyan} %s\n" "${dns_servers}"
printf "${white}DNS Response Time     :${cyan} %s\n" "${dns_response}"

printf "${reset}"
