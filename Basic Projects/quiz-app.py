import time

class Question:
    
    numberOfQuestions = 0
    numberOfCorrectQuestions = 0

    @classmethod
    def display_score(cls):
        score = 100 // cls.numberOfQuestions * cls.numberOfCorrectQuestions
        return f"{cls.numberOfQuestions} sorudan {cls.numberOfCorrectQuestions} soru bildiniz. Toplam Puanınız: {score}".center(100, "*")

    def __init__(self, _text, _choices, _answer):
        self.text = _text
        self.choices = _choices
        self.answer = _answer

    def check_answer(self):
        if (userAnswer == self.answer):
            Question.numberOfCorrectQuestions += 1
            Question.numberOfQuestions += 1 
            return f"Tebrikler cevabınız doğru, cevap {self.answer}'idi."
        else:
            Question.numberOfQuestions += 1 
            return f"Üzgünüz cevabınız doğru değil, cevap {self.answer}'idi."

question1 = Question("1) RAM bellek için aşağıdakilerden hangisi söylenemez?", ["a) Bilgilerin geçici olarak tutulduğu bellektir.", "b) RAM bellek üzerinde o an çalışan programların bilgileri yer alır.", "c) Elektrik kesildiğinde RAM bellek üzerindeki bilgiler silinir.", "d) RAM bellek aynı zamanda yardımcı bellek olarak adlandırılır."], "d")
question2 = Question("2) Aşağıdakilerden hangisi işletim sisteminin bir özelliği değildir?", ["a) Bilgisayar kapandıktan sonra da çalışarak bilgisayarı uyanık tutmak", "b) Bilgisayar donanımı ile kullanıcı arasındaki iletişimi sağlamak", "c) Çevre birimleri ile işlemci arasındaki ilişkileri düzenlemek#", "d) Bilgisayarın fiziksel yapısını kullanıma hazırlamak"], "a")
question3 = Question("3) Aşağıdaki ifadelerden hangisi yanlıştır?", ["a) Yazılım, donanımla kullanıcı arasında iletişim kuran, donanımı kontrol eden programlardır.", "b) RAM, bilgilerin geçici olarak tutulduğu, üzerinde o an çalışan programların bilgilerini tutan bellektir.", "c) Optik okuyucu bir giriş birimidir.", "d) Byte, bilgisayarda kullanılan kapasite ölçü birimlerinin en küçüğüdür."], "d")
question4 = Question("4) Veri iletmek ve bilgisayar kaynaklarını ortak kullanmak amacıyla birden fazla bilgisayarın birbirine bağlanmasına ……………………. denir.", ["a) Ağ", "b) Bağ", "c) İletişim", "d) Bağlantı"], "a")
question5 = Question("5) Aşağıdakilerden hangisi virüs çeşitlerinden değildir?", ["a) Dosya Virüsleri", "b) Solucanlar", "c) Şaka Virüsleri", "d) Kızdırma Virüsleri"], "d")

questions = [question1, question2, question3, question4, question5]

for q in questions:
    print("Sadece şıkkı yazınız!".center(100, "*"))
    print(q.text)

    for i in range(0, len(q.choices)):
        print(f"- {q.choices[i]}")

    userAnswer = input("Cevabınızı giriniz: ")
    print(q.check_answer())
    print(Question.display_score())
    time.sleep(1.7)
