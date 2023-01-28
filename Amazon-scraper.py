import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CommSpider(CrawlSpider):
    name = 'comm'
    allowed_domains = ['www.amazon.in']     #insert the allowed domain's her
    start_urls = ['https://www.amazon.in/Once-Upon-Time-Hollywood-Tarantino/dp/1398706132/ref=pd_bxgy_img_sccl_1/260-5671967-3698405?pd_rd_w=1ZeyL&content-id=amzn1.sym.d68c4347-8b80-4998-9474-4671a1e32e96&pf_rd_p=d68c4347-8b80-4998-9474-4671a1e32e96&pf_rd_r=9Q9D7A5A905HG55GXXCD&pd_rd_wg=740bV&pd_rd_r=0c3b5a7e-14d9-4db8-8d20-348927757580&pd_rd_i=1398706132&psc=1']       #insert the amazon product link inside the quotes


    le_all_reviews = LinkExtractor(restrict_css=['#reviews-medley-footer .a-text-bold', 'li.a-last>a'])  #you can change the css you want to target here
    
    
    rule1 = Rule(le_all_reviews, callback='parse_item', follow=True)  
    
    rules = (rule1,)
    
    
        
        
    def parse_item(self, response):
        
        star=response.css('.review-rating>span.a-icon-alt::text').extract()                # css selectors for the star rating
        name=response.css('#cm_cr-review_list .a-profile-name::text').extract()            # css selectors for the customer name
        review=response.css('.a-text-bold span::text').extract()                           # css selectors for the customer review
        
        
        combined = [{'star': s, 'name': n, 'review': c} for s, n, c in zip(star, name, review)]
        yield from combined


        
        


    