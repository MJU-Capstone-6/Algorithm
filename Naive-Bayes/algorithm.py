#naive_bayes + kkma
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

X = df['title']
y = df['category']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def kkma_tokenizer(text):
    kkma = Kkma()
    use_tags = ["N", "O"]  # 여러 태그를 확인할 수 있도록 리스트를 사용합니다.
    word_tag = kkma.pos(text)
    words = [word for word, tag in word_tag if (len(word) > 1) and any(tag.startswith(tag_) for tag_ in use_tags)]
    return words


vectorizer = CountVectorizer(tokenizer=kkma_tokenizer)
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# 나이브 베이즈 모델 생성 및 훈련
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train_counts, y_train)

# 테스트 데이터에 대한 예측
y_pred = nb_classifier.predict(X_test_counts)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))



# 테스트 데이터에 대한 예측
y_pred = nb_classifier.predict(X_test_counts)


print("Accuracy:", accuracy_score(y_test, y_pred))


print("Classification Report:")
print(classification_report(y_test, y_pred))
