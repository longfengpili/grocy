# @Author: longfengpili
# @Date:   2024-03-25 13:39:46
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-09-30 11:58:22

now=$(date '+%s')
now_str=$(date '+%Y-%m-%d %H:%M:%S.%3N')

logInfo() {
    lineno=$1
    message=$2
    
    logbase="$now_str - $lineno"
    echo "$logbase, 【$now】$message !!!"
}

logInfo $LINENO "start"
/usr/bin/python3 /workspace/ginfo/main.py
logInfo $LINENO "end"
