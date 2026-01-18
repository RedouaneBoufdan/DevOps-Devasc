curl http://library.demo.local/api/v1/books

curl -u cisco:Cisco123! -X POST http://library.demo.local/api/v1/books \
-H "Content-Type: application/json" \
-d '{"id":999,"title":"DevOps Exam Book","author":"Student"}'

curl -u cisco:Cisco123! -X PUT http://library.demo.local/api/v1/books/999 \
-H "Content-Type: application/json" \
-d '{"id":999,"title":"DevOps Exam Book (UPDATED)","author":"Student"}'
