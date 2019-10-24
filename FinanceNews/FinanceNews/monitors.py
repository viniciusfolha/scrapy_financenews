from spidermon import Monitor, MonitorSuite, monitors
@monitors.name("Item count")
class ItemCountMonitor(Monitor):
    @monitors.name("Minimum number of items")
    def test_minimum_number_of_items(self):
        item_extracted = getattr(self.data.stats, "item_scraped_count", 0)
        minimum_threshold = 10
        msg = "Extracted less than {} items".format(minimum_threshold)
        self.assertTrue(item_extracted >= minimum_threshold, msg=msg)

class NotFoundPage(Monitor):   
    @monitors.name("Check not found page")
    def test_not_found_page(self):
        not_found = getattr(self.data.stats, "downloader/response_status_count/404", 0)
        minimum_threshold = 0
        msg = "Page not found greater than {}.".format(minimum_threshold)
        self.assertTrue(not_found <= minimum_threshold, msg=msg)
        

class FinanceMonitorSuite(MonitorSuite):
    monitors = [ItemCountMonitor,NotFoundPage,]