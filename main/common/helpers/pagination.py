from flask import request

def page_request_args():
  page = request.args.get('page', type=int)
  per_page = request.args.get('per_page', type=int)

  return { 'page': page, 'per_page': per_page }
