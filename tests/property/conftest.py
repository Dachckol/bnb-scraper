import pytest

html_single = '<html><head></head><body>\
<div itemprop="name"><span dir="ltr"><span><h1>Property Name</h1></span></span></div>\
<div>1 bed</div>\
<div>2 bath</div>\
<section>\
    <div>\
        <header>\
            <div class="_11qg6v7y">\
                <div class="_nx4dnvl">\
                    <h1 id="dls-modal__AmenitiesModal" tabindex="-1" class="_tpbrp"><span>Amenities</span></h1>\
                </div>\
            </div>\
        </header>\
        <section>\
            <div style="margin-top: 0px; margin-bottom: 16px;">\
                <div class="_14d4n4o7">Basic</div>\
                <div style="margin-top: 24px;">\
                    <div>\
                        <div class="_2930ex">\
                            <div class="_10ejfg4u">\
                                <div class="_1cmgxhs2">Anemity 1</div>\
                            </div>\
                        </div>\
                    </div>\
                    <div>\
                        <div class="_2930ex">\
                            <div class="_10ejfg4u">\
                                <div class="_1cmgxhs2">Anemity 2</div>\
                            </div>\
                        </div>\
                        <div style="margin-top: 24px; margin-bottom: 24px;"><div class="_76irmj"></div>\
                    </div>\
                </div>\
            </div>\
        </section>\
    </div>\
</section></body></html>\
'

html_multi = '<html><head></head><body>\
<div itemprop="name"><span dir="ltr"><span><h1>Property Name</h1></span></span></div>\
<div>2 beds</div>\
<div>3 baths</div>\
<section>\
    <div>\
        <header>\
            <div class="_11qg6v7y">\
                <div class="_nx4dnvl">\
                    <h1 id="dls-modal__AmenitiesModal" tabindex="-1" class="_tpbrp"><span>Amenities</span></h1>\
                </div>\
            </div>\
        </header>\
        <section>\
            <div style="margin-top: 0px; margin-bottom: 16px;">\
                <div class="_14d4n4o7">Basic</div>\
                <div style="margin-top: 24px;">\
                    <div>\
                        <div class="_2930ex">\
                            <div class="_10ejfg4u">\
                                <div class="_1cmgxhs2">Anemity 1</div>\
                            </div>\
                        </div>\
                    </div>\
                    <div>\
                        <div class="_2930ex">\
                            <div class="_10ejfg4u">\
                                <div class="_1cmgxhs2">Anemity 2</div>\
                            </div>\
                        </div>\
                        <div style="margin-top: 24px; margin-bottom: 24px;"><div class="_76irmj"></div>\
                    </div>\
                </div>\
            </div>\
        </section>\
    </div>\
</section></body></html>\
'


@pytest.fixture(scope="module")
def page_html_single_values():
    return html_single

@pytest.fixture(scope="module")
def page_html_multi_values():
    return html_multi

