# Script
- shell

```
#!/bin/sh
echo "-----------$(date '+%Y-%m-%d')---start calculate---$(date -d yesterday '+%Y-%m-%d') data------------------------"
python ~/xiejiajun/cal_overtime/cal_daily_tasks.py $(date -d yesterday '+%Y-%m-%d')
if [[ $(date '+%d') == "01" ]];then
    echo "$(date '+%Y-%m-%d') is the first day of month, so calculate last month data"
    python ~/xiejiajun/cal_overtime/cal_month_tasks.py $(date '+%Y-%m-%d')
fi
echo "------------------------end   calculate-------------------------"
```

- dispatch

hd020的crontab无法正常使用

`0 9 * * * bash ~/xiejiajun/cal_overtime/run_cal_tasks.sh >> run.log`

只能放在Jenkins

http://hd020:8873/analysis/job/cal_overtime/
