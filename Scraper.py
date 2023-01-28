import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CommSpider(CrawlSpider):
    name = 'customer review'
    allowed_domains = ['']                                      #insert the allowed domain's here
    start_urls = ['']                                           #insert the product link inside the quotes


    le_all_reviews = LinkExtractor(restrict_css=['#reviews-medley-footer .a-text-bold', 'li.a-last>a'])     #you can change the css you want to target here
    
    
    rule1 = Rule(le_all_reviews, callback='parse_item', follow=True)  
    
    rules = (rule1,)
    
    
        
        
    def parse_item(self, response):
        
        star=response.css('.review-rating>span.a-icon-alt::text').extract()                # css selectors for the star rating
        name=response.css('#cm_cr-review_list .a-profile-name::text').extract()            # css selectors for the customer name
        review=response.css('.a-text-bold span::text').extract()                           # css selectors for the customer review
        
        
        combined = [{'star': s, 'name': n, 'review': r} for s, n, r in zip(star, name, review)]
        yield from combined


        
        


    