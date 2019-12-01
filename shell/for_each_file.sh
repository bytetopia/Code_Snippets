
# 1) change directory name
for file in ./directory_name/*
do
    if test -f $file
    then
        echo $file  # optional
        # 2) write what you want to do
    fi
done