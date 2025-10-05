### Bulk Update Rust Projects
#!/bin/bash

cmt_message=$1

for dir in rust*/; do
    (cd "$dir" && git add .; git commit -m "$cmt_message"; git push)
done

