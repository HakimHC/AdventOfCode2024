#! /bin/bash

set -e

year="2024"
day_of_month="$(date +%-d)"
url="https://adventofcode.com/${year}/day/${day_of_month}/input"
dir="day${day_of_month}"
base="templates/base.py"

test -f "cookie.txt" || (echo "Cookie file missing" 2>&1 && exit 1)
test -d "day${day_of_month}" && (echo "Day ${day_of_month} already exists" && exit 1)

cookie_content=$(cat cookie.txt)

mkdir "${dir}"

curl \
  -s \
  -o "${dir}/input" \
  -H "cookie: session=${cookie_content};" \
  "$url"

cp "${base}" "${dir}/main.py"
touch "${dir}/test"

echo "Ready for day ${day_of_month}. Let's go"