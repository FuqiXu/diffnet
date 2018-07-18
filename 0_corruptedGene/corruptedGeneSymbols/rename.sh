ls | while read file; do
     new=$( echo $file | sed 's/[^0-9]*\([^ ]*\)[^.]*\(\..*\)*/object\1\2/' )
     mv "$file" "$new"
done