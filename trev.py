html_content = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Тревога</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }
        .tyo {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            font-family: 'Bahnschrift SemiBold SemiCondensed', Arial, sans-serif;
            color: #3a3b38;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: white;
            margin: 0;
            padding: 0;
        }
        .container pre {
            font-size: 18px;
            font-family: Arial, sans-serif;
            white-space: pre-wrap;
            margin: 0;
            color: #333;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px;
            position: relative;
            bottom: 0;
            width: 100%;
        }
        img {
            max-width: 100%;
            height: auto;
            margin: 10px 0;
        }
        header {
            background-color: #007BFF;
            color: white;
            padding: 20px;
            text-align: center;
        }
        nav {
            background-color: #333;
            padding: 10px;
            text-align: center;
        }
        nav a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
            font-weight: bold;
        }
        nav a:hover {
            text-decoration: underline;
        }
        .iot {
            font-size: 18px;
            font-weight: bold;
            font-family: 'Bahnschrift SemiBold SemiCondensed', Arial, sans-serif;
            color: #e9fa34;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        ul {
            list-style-type: disc;
            padding-left: 40px;
            text-align: left;
        }
        ul li {
            margin-bottom: 10px;
        }
        .info-container {
            background-image: url('page3_gradient.jpg'); /* Замените на путь к вашей картинке */
            background-size: cover; /* Растягиваем изображение на весь блок */
            background-position: center; /* Центрируем изображение */
            border-radius: 15px; /* Закругленные углы */
            padding: 20px;
            margin: 20px auto;
            max-width: 800px;
            position: relative;
            color: #333; /* Цвет текста для контраста */
        }
        .info-container h2 {
            text-align: center;
            font-weight: bold;
            font-size: 24px;
            font-family: 'Bahnschrift SemiBold SemiCondensed', Arial, sans-serif;
            color: #333;
        }
        .info-container p {
            font-size: 16px;
            color: #555;
            line-height: 1.6;
        }
        .triangle {
            width: 0;
            height: 0;
            border-left: 20px solid transparent;
            border-right: 20px solid transparent;
            border-top: 20px solid #e0f7ff;
            position: absolute;
            bottom: -20px;
            left: 50%;
            transform: translateX(-50%);
        }
        .cinter {
            display: flex;
            flex-direction: column;
            background-color: green;
            margin: 20px auto;
            padding: 20px;
            border-radius: 15px;
            max-width: 800px;
            color: white;
        }
        .cinter h2 {
            text-align: center;
            font-size: 24px;
            font-family: 'Bahnschrift SemiBold SemiCondensed', Arial, sans-serif;
            margin-bottom: 20px;
        }
        .cinter p {
            font-size: 16px;
            line-height: 1.6;
        }
        .cloud-container {
            display: flex;
            justify-content: space-around;
            margin: 20px;
        }
        .cloud-left {
            width: 45%;
            background-image: url('phone_gradient.jpg');
            background-size: cover;
            clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%, 0 80%, 20% 60%, 0 40%);
            border-radius: 0 0 20px 20px;
            padding: 20px;
            color: white;
            text-align: justify;
        }
        .cloud-right {
            width: 45%;
            background-image: url('phone_gradient.jpg');
            background-size: cover;
            clip-path: polygon(0 0, 100% 0, 100% 40%, 80% 60%, 100% 80%, 100% 100%, 0 100%);
            border-radius: 20px 20px 0 0;
            padding: 20px;
            color: white;
        }
        .cloud-glava {
            width: 100%;
            background-image: url('oblako.jpg');
            background-size: cover;
            border-radius: 0 0 20px 20px;
            padding: 20px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        }
    </style>
</head>
<body>
    <header>
        <div class="cloud-glava">
            <h1>Психологическая помощь ВЫХОД ЕСТЬ!</h1>
            <img src="page_psih2.png" alt="Логотип компании">
        </div>
    </header>
    <nav>
        <a href="index.html">Главное</a> <a href="reg_and_login.html">Услуги</a>
    </nav>

    <!-- Новые контейнеры с нестандартными формами -->
    <div class="cloud-container">
        <div class="cloud-left">
            <div class="tyo">Тревога</div>
            <div class="iot">
                <pre>
                    Тревога - отрицательно окрашенная эмоция,
                    выражающая ощущение неопределённости,
                    ожидание негативных событий, 
                    труднопреодолимые предчувствия.
                    Психическая и физическая реакция 
                    на ощущаемую угрозу.
                    Может помогать в защите от опасности, 
                    помогает сосредоточить внимание на проблеме.
                    Если тревога слишком сильная или слишком частая, 
                    то она может нарушать жизнь человека,
                    проявляться тревожным расстройством.
                </pre>
            </div>
        </div>
        <div class="cloud-right">
            <div class="tyo">Симптомы тревоги:</div>
            <div class="iot">
                <ul>
                    <li>Неконтролируемое беспокойство.</li>
                    <li>Дискомфорт в животе.</li>
                    <li>Мышечное напряжение.</li>
                    <li>Дрожь в теле.</li>
                    <li>Невозможность расслабиться.</li>
                    <li>Головная боль, головокружение.</li>
                    <li>Трудности концентрации внимания.</li>
                    <li>Чрезмерная нервозность, волнение.</li>
                    <li>Ускоренное сердцебиение, учащенное дыхание.</li>
                    <li>Проблемы со сном.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- Контейнер "Как нарастает тревога?" -->
    <div class="container">
        <div class="info-container">
            <h2>Как нарастает тревога?</h2>
            <p>
                Тревога или страх заставляют человека избегать тех ситуаций или предметов, которые вызывают страх. 
                В результате избегания на какое-то время наступает кратковременное облегчение, но следующая встреча 
                с объектом тревоги может быть гораздо более пугающей. Таким образом может образоваться порочный 
                круг избегания и усиления тревоги.
            </p>
            
        </div>
    

        <!-- Контейнер "Как лечатся тревожные расстройства?" -->
        <div class="info-container">
            <h2>Как лечатся тревожные расстройства?</h2>
            <p>
                <strong>Психотерапия.</strong> Например, может использоваться когнитивно-поведенческая терапия. 
                Во время сессий выявляются и прорабатываются искажения мышления, провоцирующие тревогу. Также 
                эффективен метод экспозиции, при котором психотерапевт и пациент создают план по постепенному 
                противостоянию тревожащим ситуациям и таким образом разрывают порочный круг тревоги. При таком 
                активном противостоянии страхи теряют свою силу.
            </p>
            <p>
                <strong>Медикаментозная помощь</strong> (по назначению врача могут использоваться такие лекарственные 
                средства, как антидепрессанты и др.).
            </p>
        </div>
        
    </div>

    <!-- Контейнер "Самопомощь при тревоге" -->
    <div class="container">
        <div class="cinter">
            <h2>САМОПОМОЩЬ ПРИ ТРЕВОГЕ</h2>
            <p>
                Техники "заземления" позволяют взять эмоции под контроль, оказать скорую помощь при тревоге, сильном страхе. 
                Используя "заземление", человек, испытывающий волнение, беспокойство, может вернуться от тягостных мыслей, 
                нахлынувших чувств в ситуацию "здесь и сейчас". Удерживая свое внимание на реальном объекте.
            </p>
            <p>
                Существует множество техник заземления, использовать их можно практически в любых ситуациях и местах:
            </p>
            <ul>
                <li>Посмотрите вокруг себя. Назовите (можно про себя) пять вещей, которые Вы видите, четыре, которые Вы можете потрогать, три, которые Вы слышите, две, которые можете понюхать и одну, которую Вы можете почувствовать на вкус.</li>
                <li>Держите при себе небольшой предмет, чтобы в ситуации стресса Вы могли взять его в руки. Это может быть что-то вроде гладкого камня, отполированного кусочка стекла или украшения; это может быть маленькая статуэтка или что-то, что связано у Вас с хорошими воспоминаниями. Носите этот объект с собой там, где его легко хранить, и доставайте, когда тревога, беспокойство захлестывают Вас. Обращайте внимание и описывайте в уме каждую деталь объекта, дотрагиваясь до него рукой и отмечая все ощущения от этого касания (текстура, размер, вес, температура и др.).</li>
                <li>Буквально "заземлитесь". Если Вы стоите или сидите, отметьте, как ваши стопы стоят на полу, почувствуйте в прямом смысле почву под ногами и силу земного притяжения. Вы можете встать, снять обувь и наступать каждой ногой на землю или на пол, ощущая, как будто Ваши ноги — это основание добротного здания, крепко связанного с землей.</li>
                <li>Выйдите на улицу или посмотрите в окно, найдите любой объект, например дерево, растение. Отметьте как можно больше деталей этого объекта. Например, отметьте, как на дерево падает свет и куда отбрасывается тень. Рассмотрите, какие у него ветви, есть ли на них почки или листья, какой они формы, цвета.</li>
            </ul>
        </div>
    </div>

    <footer>
        <img src="page_psih2.png" alt="фото">
        <pre>
            ООО «Медико-диагностический центр «Выход Есть!» - это многопрофильное лечебно-профилактическое учреждение, которое имеет современную материально-техническую базу,
            оказывает платные медицинские услуги и осуществляет консультации высококвалифицированных специалистов.
        </pre>
        <pre>
            Обращаем ваше внимание на то, что данный интернет-сайт носит исключительно информационный характер и ни при каких условиях не является публичной офертой,
            определяемой положениями ст. 405 Гражданского кодекса Республики Беларусь.
            Для получения подробной информации о наличии и стоимости указанных услуг, пожалуйста, обращайтесь к администраторам клиники.
        </pre>
    </footer>
</body>
</html>
"""

with open("trev.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML-файл успешно создан!")
