from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser

# 서버 포트 설정
port = 8000

# 서버 시작
server_address = ('', port)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print(f'서버가 포트 {port}에서 실행 중입니다...')

# 브라우저에서 자동으로 페이지 열기
webbrowser.open(f'http://localhost:{port}/02_html_tag.html')

# 서버 실행
httpd.serve_forever() 