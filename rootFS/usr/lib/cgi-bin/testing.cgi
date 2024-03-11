#!/bin/bash

 aCPU_CUR_FREQ=()
        aCPU_MIN_FREQ=()
        aCPU_MAX_FREQ=()
        Obtain_Cpu_Freq()
        {
                for ((i=0; i<$G_HW_CPU_CORES; i++))
                do
                        [[ -f /sys/devices/system/cpu/cpu$i/cpufreq/scaling_cur_freq ]] && read -r aCPU_CUR_FREQ["$i"] < "/sys/devices/system/cpu/cpu$i/cpufreq/scaling_cur_freq"
                        [[ -f /sys/devices/system/cpu/cpu$i/cpufreq/scaling_min_freq ]] && read -r aCPU_MIN_FREQ["$i"] < "/sys/devices/system/cpu/cpu$i/cpufreq/scaling_min_freq"
                        [[ -f /sys/devices/system/cpu/cpu$i/cpufreq/scaling_max_freq ]] && read -r aCPU_MAX_FREQ["$i"] < "/sys/devices/system/cpu/cpu$i/cpufreq/scaling_max_freq"
                done
        }

        CPU_TEMP_PRINT=
        Obtain_Cpu_Temp(){ CPU_TEMP_PRINT=$(print_full_info=1 G_OBTAIN_CPU_TEMP); }

        CPU_GOV_CURRENT='N/A'
        Obtain_Cpu_Gov(){ [[ -f '/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor' ]] && read -r CPU_GOV_CURRENT < /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor; }

        Print_Stats()
        {
                echo -e "\n \e[38;5;154m─────────────────────────────────────────────────────\e[0m\n \e[1mDietPi CPU Info\n\e[90m Use dietpi-config to change CPU / performance options\e[0m\n \e[38;5;154m──────────────────────────────────>

                (( $G_HW_MODEL == 20 )) && echo -e '\n\e[90m[\e[93mWARNING\e[90m] \e[97mMost CPU info is not available on virtual machines.\e[0m\n'

                echo -e " Architecture \e[90m|\e[0m     $G_HW_ARCH_NAME
 Temperature  \e[90m|\e[0m     $CPU_TEMP_PRINT
 Governor     \e[90m|\e[0m     $CPU_GOV_CURRENT"

                if [[ $CPU_GOV_CURRENT == 'ondemand' || $CPU_GOV_CURRENT == 'conservative' ]]
                then
                        echo -e " Throttle up  \e[90m|\
exit 0
