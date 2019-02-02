# -*- coding: UTF-8 -*-
# 朴素贝叶斯实战

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import nltk
import jieba


# # TF-IDF值计算
# tfidf_vec = TfidfVectorizer()
# documents = [
#     'this is the bayes document',
#     'this is the second second document',
#     'and the third one',
#     'is this the document'
# ]
# tfidf_matrix = tfidf_vec.fit_transform(documents)
# print('不重复的词：', tfidf_vec.get_feature_names())
# print('每个单词的ID：', tfidf_vec.vocabulary_)
# print('每个单词的tfidf值：', tfidf_matrix.toarray())

# # 分档分类
# # topic1 对文档分词
# word_list = nltk.word_tokenize(text)
# nltk.pos_tag(word_list)
# word_list = jieba.cut(text)
#
# # topic2 加载停用词表
# stop_words = [line.strip().decode('utf-8') for line in io.open('stop_word.txt').readlines()]
#
# # topic3 计算单词的权重
# tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5)
# features = tf.fit_transform(train_contents)
#
# # topic4 生成朴素贝叶斯分类器
# clf = MultinomialNB(alpha=0.001).fit(train_features, train_labels)
#
# # topic5 进行预测
# test_tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5, vocabulary=train_vocabulary)
# predicted_labels = clf.predict(test_features)
#
# # topic6 计算准确率
# print(metrics.accuracy_score(test_labels, predicted_labels))

