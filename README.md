알고리즘 진행상황

<img width="347" alt="result" src="https://github.com/MJU-Capstone-6/Algorithm/assets/54893409/1025d502-b5b7-4264-869f-33b340e58f1a">


기존의 나이브 베이즈의 성능으로는 평균 정확도 0.85의 성능을 보임 
문장의 전처리나 다른 방식을 사용해 전체 평균 정확도 0.9까지 높이는 걸로 목표

# 4/20 



기존에 있던 카테고리말고도 추가 카테고리를 넣어서 데이터의 양을 늘렸다.     

![image](https://github.com/MJU-Capstone-6/Algorithm/assets/54893409/5ce40680-9f8b-4881-b68e-9c691cb71667)  
마찬가지로 같은 코드로 돌렸더니 아래와 같은 정확도가 나왔음   
Counter vectorizer사용  
![image](https://github.com/MJU-Capstone-6/Algorithm/assets/54893409/5a7a8b6a-aeef-442e-84a3-fe6fe19bb1e4)  

Tfidf 의 방식을 적용해보았더니 아래와 같은 정확도로 나왔다.   
![image](https://github.com/MJU-Capstone-6/Algorithm/assets/54893409/06f9501e-3d41-4e87-98f8-2269dbb3fc22)   
Tfidf를 본 결과 아예 구분을 못하는 경우(ruby)도 존재하여 일단은 CountVectorize 를 사용하기로 했다



c++ 이랑 c#에서 엄청 낮은 정확도로 인해 전체 정확도가 많이 떨어져있는데(c# 0.07, c++ 0.14) 아마도 csv를 불러올때 특수문자를 빼서 #, ++ 같은 기호가 사라진걸로 추측되어 특수문자 + 숫자를 빼서 그런걸로 보임

![image](https://github.com/MJU-Capstone-6/Algorithm/assets/54893409/44136f93-b7d3-4e7a-b24c-a41a7661bd2d)

여전히 특수문자 처리를 해도 수치가 나아지지 않아 데이터를 직접 확인   
## c++ 
![image](https://github.com/MJU-Capstone-6/Algorithm/assets/54893409/35da1e7b-eb01-40fc-aca6-6b08e457f2cb)

![image](https://github.com/MJU-Capstone-6/Algorithm/assets/54893409/5668d3ba-0d73-4f21-94c3-aede69dd063a)  

## c# 
![image](https://github.com/MJU-Capstone-6/Algorithm/assets/54893409/543795f1-e08b-439e-b6de-86eaffaac83c)  
대부분의 데이터가 우리가 원하는 코드와 관련없는 것으로 판단

애초에 크롤링 할때 c언어로 크롤링을 해야된다고 판단되어 다시 크롤링(아래의 사진은 크롤링해서 만든 dataframe이다)  

![image](https://github.com/MJU-Capstone-6/Algorithm/assets/54893409/9b3aabf2-2f13-4e53-93d8-0cc6d8849b58)  
![image](https://github.com/MJU-Capstone-6/Algorithm/assets/54893409/3ae71000-f916-4674-8a7b-3a2e2e6aba7b)  
전체 갯수는 줄어들었지만 그래도 충분한 양이라 판단되어 진행  



결과는 아래와 같이 나왔다.   

![image](https://github.com/MJU-Capstone-6/Algorithm/assets/54893409/67012c45-e6f9-40ea-9d0d-69b7b36e6f4e)  

전체 평균이 약 0.77로 나왔다.   
성능을 끌어 올려서 목표치는 0.9가 아닌 0.85로 수치 재조정



# 4/24

알고리즘 성능 개선 
konlpy에 있는 kkma를 통해 문장에서 명사, 외국어 명사를 추출 & 토큰화 시켜 성능을 끌어올림.   

![image](https://github.com/MJU-Capstone-6/Algorithm/assets/54893409/07377cc3-ab4c-4b92-a1fb-6df5502c985d)
