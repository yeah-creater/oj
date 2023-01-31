namespace py judge_service

service Judge {
    string judge_code(1: string info,2: string other),
}