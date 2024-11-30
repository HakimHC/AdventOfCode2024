#! /bin/bash

set -e

year="2024"
day_of_month="$(date +%d)"
url="https://adventofcode.com/${year}/day/${day_of_month}/input"
dir="day${day_of_month}"
base="templates/base.py"

mkdir "${dir}"
curl -s "$url" -o "${dir}/input"
cp "${base}" "${dir}/main.py"

echo "Ready for day ${day_of_month}. Let's go"