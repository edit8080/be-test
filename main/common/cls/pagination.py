class Pagination: 
  def __init__(self, page, per_page):
    self.page = page
    self.per_page = per_page

  def set_pagination(self, sqlQuery):
    if (self.page or self.per_page): # page, per_page 중 하나라도 명시하면 페이지네이션된 데이터
      results = sqlQuery.paginate(self.page or 1, self.per_page or 20)
      return { 'items': results.items, 'page': results.page, 'total': results.total }

    else: # page, per_page 를 명시하지 않으면 전체 데이터
      results = sqlQuery.all()
      return { 'items': results, 'page': 1, 'total': len(results) }
