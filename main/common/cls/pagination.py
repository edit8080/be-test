class Pagination: 
  def __init__(self, page, per_page):
    self.page = page
    self.per_page = per_page

  def set_pagination(self, sqlQuery):
    if (self.page or self.per_page):
      results = sqlQuery.paginate(self.page or 1, self.per_page or 20)
      return { 'items': results.items, 'page': results.page, 'total': results.total }
    else:
      results = sqlQuery.all()
      return { 'items': results, 'page': 1, 'total': len(results) }
