import requests
store_list = ['sandisk','kenvue','welcare-thailand']
for store in store_list:
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,id;q=0.8,zh-CN;q=0.7,zh-TW;q=0.6,zh;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://www.lazada.co.th',
        'priority': 'u=1, i',
        'referer': 'https://www.lazada.co.th/shop/sandisk',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
        'x-requested-with': 'XMLHttpRequest',
        # 'cookie': 't_fv=1756130630807; t_uid=O0HKoqvWzswE1UJn1Or1LPHVwwjzdB5I; t_sid=Xb5WLmAWbNihNiYICA68ZqLJ9qLBPTOG; utm_channel=NA; cna=SFszISblkCUCASRHOomg4g4B; hng=TH|en|THB|764; _m_h5_tk=28940e957ece232308971e16c0324ca7_1756138193381; _m_h5_tk_enc=cc2bc5af7004ff45dc38605fea3e0115; lzd_cid=f94fd6c7-4dad-4696-b7d2-129ce1195ded; lzd_sid=17aa80faca83a8378d39c3e82847391a; _tb_token_=78d187073b95a; lwrid=AgGY4YsHXISmgB2JcO4hX39uI61J; lwrtk=AAIEaKzd0l6/imR0CJy67N5hK4dfGLl+P6xKGIhpOoVZCMM598trhrY=; xlly_s=1; _gcl_au=1.1.800247407.1756130649; _ga=GA1.3.2112541798.1756130677; _gid=GA1.3.612709164.1756130677; _fbp=fb.2.1756130676954.780407014956393980; _ga_HKW7PMMCHF=GS2.3.s1756130676$o1$g1$t1756130677$j59$l0$h0; _uetsid=6f5cc87081bc11f086a3a17b107662be; _uetvid=6f5cd00081bc11f0a714b1f480b1a880; cto_bundle=yfi6_F9tdFZEOVpXYjNSeTk5bDR1ekRTQmRXd0IlMkZocU5BSGdRUDJHNkxDZHBVVndHbFdidWpGRWhnTUEzMDVORVFIZWJoR0ZJTHo4NVlmRHV2STE0MmhQWGZpNkM1T1dEMnhrbFBzUElYUHVVWThyQ1lCTTdVdCUyQm4zNExyJTJGbzdXbWJPSlRLWGxJWjRIYWFJRE95R2U0ZlF1TjVRVU1JakVLdExRY3R2Z1VwVFhKbDglM0Q; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C20326%7CMCMID%7C01562542876520714063081055200717454320%7CMCAAMLH-1756735478%7C3%7CMCAAMB-1756735478%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1756137878s%7CNONE%7CvVersion%7C5.2.0; isg=BPf3kuneU2L4TNfuVKBRfxCvhutBvMseb3Qr_kmlzUdP-BU6UY4ab9iZ3kCmEKOW; tfstk=g67Kn_iMCR2Hs2HE9TqiZHUMOYVgIlfEW95jrLvnVOBOGskHVTqUVUBVe3_H-_OSwd1PEpYkRLTRBt1n-9bRb4CVawVerW8FTU87n-4De65ezdCdQXyG17OyyBwUuAy1TU87IR2een5FLRt3_UT76FOWN2TSA3NT5QvsRQgBNAN9adTSRB9Q5VOk9LGBVT1_6QJ6FUtCFhN9ad9WPUGWM8psOL0RvRNXeGg2C4g5WBK_o69sRI799H9fOw3SPbRpvK1BCJTXF9t1a3Qra4KROiWyG9MQnH55XOdpyPmBl1I5HC7QovdNx11DCshrz68pwnTWXbg56eJ6cw8blAdNf6j589h-PB7ho3p2X7gyqF_Dci6KaS56RQ6y0a2q8p15gZSDkPmBl1I5HgIznZbAMDDDHQmQ65nr4HOZg4mLMr-F1UR9nWU-40-a_Cp065nr4HOw6KVLw0oyb55..; epssw=10*kn6ss6DIE3szzOxeb-D0qqFF37icoVrXAkKV2RXQt-iQONMoU7D0jN30bRFebCssb-D0UDij0Jr9YOGjOuZN_He46yIyQuU-7BWYtOO20YfOOahsGREMDRnQ-pFy0fgpCslCbMCQ1LrYtQrfCHssCHMwAwh3da6aF6FODQEEx1f8tOXbfTgRulvuEEFZQEQ0VMtsdHrgRr6dPtnqnpPOSCpDmWng02ebVrBKt_GNoRxebRDfcWFasssssRFai9bFO3subNiae1SPskiaG7uAmFgOqnlFH0KdS7rNdz2B88N2F_aOiJswcWKjEXA6wTmYt2i3c1a.',
    }

    response = requests.get('https://member.lazada.co.th/user/api/getCsrfToken', headers=headers)
    csrf = response.json()['module']['token']

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,id;q=0.8,zh-CN;q=0.7,zh-TW;q=0.6,zh;q=0.5',
        'priority': 'u=1, i',
        'referer': 'https://www.lazada.co.th/',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
        'x-csrf-token': csrf,
        # 'cookie': '__wpkreporterwid_=2d8cc16f-d470-4557-12ad-2edec62255e7; t_fv=1756130630807; t_uid=O0HKoqvWzswE1UJn1Or1LPHVwwjzdB5I; t_sid=Xb5WLmAWbNihNiYICA68ZqLJ9qLBPTOG; utm_channel=NA; cna=SFszISblkCUCASRHOomg4g4B; hng=TH|en|THB|764; userLanguageML=en; _m_h5_tk=28940e957ece232308971e16c0324ca7_1756138193381; _m_h5_tk_enc=cc2bc5af7004ff45dc38605fea3e0115; lzd_cid=f94fd6c7-4dad-4696-b7d2-129ce1195ded; lzd_sid=17aa80faca83a8378d39c3e82847391a; _tb_token_=78d187073b95a; EGG_SESS=S_Gs1wHo9OvRHCMp98md7FPCR_XIAyTLaapebu32kmg9_PF9J1o6tPNOCGHpANwMiqZVEIYiuG3FhZXADNVaa-MmoUEDfeqqQ5FKh-tnP2GNXimzUSCHHFZ_ghEFqKvLD9DnMdE_T3GSTMop_yxh6hmIPiUK0QETfw710gbZSsM=; lwrid=AgGY4YsHXISmgB2JcO4hX39uI61J; lwrtk=AAIEaKzd0l6/imR0CJy67N5hK4dfGLl+P6xKGIhpOoVZCMM598trhrY=; xlly_s=1; _gcl_au=1.1.800247407.1756130649; _bl_uid=47m2hejqr8p6y1u76gORu4m55tI9; __itrace_wid=cae6c600-a412-4616-b3aa-ae348bade4c3; _ga=GA1.3.2112541798.1756130677; _gid=GA1.3.612709164.1756130677; _fbp=fb.2.1756130676954.780407014956393980; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C20326%7CMCMID%7C01562542876520714063081055200717454320%7CMCAAMLH-1756735478%7C3%7CMCAAMB-1756735478%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1756137878s%7CNONE%7CvVersion%7C5.2.0; JSESSIONID=2E0CF65E608BB0069EAC3FB1B0978D18; _uetsid=6f5cc87081bc11f086a3a17b107662be; _uetvid=6f5cd00081bc11f0a714b1f480b1a880; cto_bundle=2P0B8F9tdFZEOVpXYjNSeTk5bDR1ekRTQmRSWmRGNmdQbWN1T2oyUmVLJTJCVDJidVZnWjA1VDczUTgxZ1hIa3lVMTJJem5GWHZYT1lQeHg5dDlBOFkyaVF5TiUyRmh3SnU5M25QdlJOZzNnRkdncFZ4a0ZJY0lSd3FKdXJkNFBjdkNzV0VxTzRmM0Y4WTgwYWo4TzQzdkt0V24lMkIzcUpvQWdUZ0RTaGREYjNJYUFrRGFjTm8lM0Q; _ga_HKW7PMMCHF=GS2.3.s1756130676$o1$g1$t1756131085$j60$l0$h0; isg=BD4-TE252kWrfQ5hdcOIeKF8j1SAfwL5XqfSsehFQAG_i9xlUA58CE0oA09Hs_oR; epssw=10*WZ1ss6CbJBlNImD6bRFeOw394I3PVjFfsxKD97D0t-iQO-PJU7u0j-XQO-XebUug-PVYukWvojCn_3EYESkjQRCNxfZPXR1sCgUHXRWJQHS2BVrtY1sVzFFOOOt1usuuJqNMfbAB5SFOOOtPGZEe57HCOP9i0iB5El-CecVvHk9P76AvMcZGsiUvo1ftOiwXuCNwQ3oMVjpHtdEDA66VO-X9e1Xzsssss7VZssFtssOa1IuStOFxSWIbB6spbWUyMvQ4v0DGd0UcnoJGqazEa2Q2aeaSMZM2bvCHHgeTTM81kJuFNa..; tfstk=gGsrRqM7puEz3IlbVsKE_-KqdktJvHP_tMOBK9XHFQAuy7dh0sOXA83Qyp-eg6dW-BsCgvJ6MUiBVH_4L667eMaRKBDFi9YnVTaJ-pAVKpO79LOeK9AXF4sFpDJhK6eJO8UfeTKpx5N6Tl6ReDnvQ3VXxJXDAp8Q6szfeTKKH5N_fl6-LSCvWQxhtnYDQpKHEUfHmqAvppckK02VnIdmtBvnroXDQp0HxHfhn-JpiLxH-6X03pdDtbhGE9m2CU20zWwX64i60CXkgDmZML8kGldqx0s2UtRGEPmnxiJyzi0GvRwpPwX9Wg6UYmK5QZxDCTEr0hXkQ_Ofslm2mt6cOFQY9cTAgM8OqUHnrtSeaFjkuviO339hte7Y_c9yVZ8N4aeKiTf6aNxRdAP53F72WKYmL4x55OspSgqr6IT9L_Ofslm2mejyFXp0kqIdzX0HrKp21-y2gdBcJVNfL9uKJEx93CwWF23prKp21-yqJ2LDBKR_FL1..',
    }

    params = {
        'ajax': 'true',
        'from': 'wangpu',
        'isFirstRequest': 'true',
        'langFlag': 'en',
        'page': '1',
        'pageTypeId': '2',
        'q': 'All-Products',
    }

    response = requests.get(f'https://www.lazada.co.th/{store}/', params=params, headers=headers)
    items = response.json()['mods']['listItems']
    with open(f'{store}.txt', 'w', encoding='utf-8') as f:
        for item in items:
            sold = item['itemSoldCntShow'] if 'itemSoldCntShow' in item else '0'
            f.write(f"{item['name']}|{item['image']}|{sold}\n")