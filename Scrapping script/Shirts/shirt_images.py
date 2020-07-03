def scrap_image_url(driver):
    images=driver.find_elements_by_xpath("//img[@class='s-image']")
    brands=driver.find_elements_by_xpath("//div[@class='a-row a-size-base a-color-secondary']")
    product_description=driver.find_elements_by_xpath("//a[@class='a-link-normal a-text-normal']")

    product_data={}
    product_data['image_urls']=[]
    product_data['brands']=[]
    product_data['product_description']=[]

    for image in images:
        source=image.get_attribute('src')
        product_data['image_urls'].append(source)

    for brand in brands:
        product_data['brands'].append(brand.text)

    for product_desc in product_description:
        product_data['product_description'].append(product_desc.text)

    print("Returning scraped data")

    return product_data
