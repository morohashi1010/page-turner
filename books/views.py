from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Page Turner へようこそ！</h1><p>ここは本の一覧画面になる予定のページです。</p>") 

def book_detail(request, book_id):
    return HttpResponse(f"<h1>本の詳細画面 (本ID: {book_id})</h1><p>ここにカバー画像やレビュー一覧が表示されます。</p>")

def submit_review(request, book_id):
    return HttpResponse(f"<h1>レビュー投稿受付</h1><p>本ID: {book_id} へのレビュー（0〜10点）を受け付けました！(仮処理)</p>")
