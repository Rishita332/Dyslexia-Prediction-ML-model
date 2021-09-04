import streamlit as st
#import fetch

def main():
#    fetch.front_up()

    st.markdown("""
        <header>
        <br>
        <span style="background-color: #e9eef0;font-weight: 100;font-size: 30px;opacity: 0.7;padding: 10px;transition: cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.5s;">Home</span>
        <span style="background-color: #e9eef0;font-weight: 100;font-size: 30px;opacity: 0.7;padding: 10px;transition: cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.5s;"><a href="quiz.html">Quiz</a></span>
        <span style="background-color: #e9eef0;font-weight: 100;font-size: 30px;opacity: 0.7;padding: 10px;transition: cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.5s;"><a href="survey.html">Survey</a></span>
        <span id="last" style="background-color: #e9eef0;font-weight: 100;font-size: 30px;opacity: 0.7;padding: 10px;transition: cubic-bezier(0.25, 0.46, 0.45, 0.94) 0.5s;">Signup</span>
        </header>
        <div style="background-image:url("dyslexia.png"); min-height:400;background-attachment:fixed;background-position:center;background-repeat:no-repeat;background-size:cover;"></div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div style="background-color: #73b7c9dd;font-size: 20px;font-weight: 100;text-align: center;padding: 2em;">
        <centre><i style="font-size: 40px;font-weight: 20;background-color: rgba(245, 245, 245, 0.5);">"Children are a nation's most valuable assets!"</i></centre><br><br>
        Learning disabilities are disorders that affect the ability to understand or use spoken or written language, do
        mathematical calculations, coordinate movements, or direct attention. Learning disabilities have nothing to do
        with
        how smart a person is. Rather, a person with a learning disability may just see, hear, or understand things
        differently.
        That can make everyday tasks, such as studying for a test or staying focused in class, much more difficult.
        There
        are strategies a person can learn to make it easier
        to cope with these differences.<br>
        It's important to note that attention deficit hyperactivity disorder (ADHD) and autism spectrum disorders are
        not
        the same as learning disabilities. There are many different kinds of learning disabilities, and they can affect
        people differently. </br>
        </div>
        <div style="background-image:url("bg.jpeg"); min-height:300;background-attachment:fixed;background-position:center;background-repeat:no-repeat;background-size:cover;"></div>
        <div style="background-color: #c5e0e8;font-size: 20px;font-weight: 100;padding: 1em;">
        <h3>Dyslexia</h3>
        Dyslexia is a language processing disorder that impacts reading, writing, and comprehension. Dyslexics may
        exhibit
        difficulty decoding words or with phonemic awareness, identifying individual sounds within words. Dyslexia often
        goes diagnosed for many years and often results in trouble with reading, grammar, reading comprehension, and
        other
        language skills.
        <h3>Signs and Symptoms</h3>
        Dyslexia impacts people in different ways. So, symptoms might not look the same from one person to another. A
        key
        sign of dyslexia is trouble decoding words. This is the ability to match letters to sounds. Kids can also
        struggle
        with a more basic skill called phonemic awareness. This is the ability to recognize the sounds in words. Trouble
        with phonemic awareness can show up as early as preschool.

        <h3>Possible Causes of Dyslexia</h3>
        Researchers haven't yet pinpointed exactly what causes dyslexia. But they do know that genes and brain
        differences
        play a role. Here are some of the possible causes of dyslexia:<br>
        <ul>
            <li>
                <b>Genes and heredity:</b> Dyslexia often runs in families. About 40 percent of siblings of people with
                dyslexia also
                struggle with reading. As many as 49 percent of parents of kids with dyslexia have it, too. Scientists
                have also
                found genes linked to problems with reading and processing language.
            </li><br>
            <li>
                <b>Brain anatomy and activity:</b> Brain imaging studies have shown brain differences between people
                with and without
                dyslexia. These differences happen in areas of the brain involved with key reading skills. Those skills
                are
                knowing how sounds are represented in words, and recognizing what written words look like.
            </li>
        </ul>
        <h3>How reading with Dyslexia looks like?</h3>
        <img src="dyslexia.gif" width="700">
        </div>
        <div style="background-color: #73b7c9dd;font-size: 20px;font-weight: 100;text-align: center;padding: 2em;">
        <h1>
            <centre><b> How do you know if you are dyslexic? </b></centre><br>
        </h1>
        We have developed a Machine Learning Model that predicts whether a person is dyslexic or not? All you need to do
        is take a quick survey and a quiz.<br>
        <br>
        <span><a href="survey.html">Take Survey</a></span>
        <span><a href="quiz.html">Take Quiz</a></span>
        </div>
        <div style="background-image: url("trial.jpeg");min-height: 300px;background-attachment: fixed;background-position: center;background-repeat: no-repeat;background-size: cover;"></div>
        <footer>
        2021 WEBpredictor<br>
        All rights reserved<br>
        Issued in public interest<br>
        WEBpredictor does not provide any medical advice, diagnosis or treatment.<br><br>
        </footer>
        """, unsafe_allow_html=True)