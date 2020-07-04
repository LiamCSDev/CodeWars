# TODO: complete this class

class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self.items_per_page = items_per_page
      self.collection = collection
  
  # returns the number of items within the entire collection
  def item_count(self):
      return len(self.collection)
  
  # returns the number of pages
  def page_count(self):
      return round(self.item_count() / self.items_per_page) + 1
	
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
      if self.page_count() -1 < page_index or page_index < 0: 
          return -1
      elif self.item_count() - self.items_per_page * page_index > self.items_per_page:
          return self.items_per_page
      else:  
          return self.item_count() - self.items_per_page * page_index 
  
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
      if item_index < 0 or item_index >= self.item_count() or not self.item_count():
          return -1
      else: 
          page = 0
          while item_index >= self.items_per_page:
              item_index -= self.items_per_page
              page += 1

          return page

collection = range(1,25)
helper = PaginationHelper(collection, 10)
print(helper.item_count())
print(helper.page_count())
print(helper.page_item_count(-6))
print(helper.page_index(9))