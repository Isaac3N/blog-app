import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css'
import { Formik } from 'formik';

const Home = () => (
    <div className='container'>
        <div class="grid-container">
            <div class="navigation"><h3>This is a Navigation</h3></div>
            <div class="Introduction">
                <h2>Hey Friends! I am Isaac Ndubuisi, a full-stack developer.</h2>
                <strong><h4>
                    I play chess, read books that interest me, code, write technical articles and wannabe full time django and react fan boy but 
                    on my free Time I am student trying to get by :&#41;
                    <br/> 
                    I try to write weekly articles on the following and more! 
                    So please subscribe to my only friends newsLetter and we would be best friends forever and that is a promise &#128521;
                </h4></strong>
                <div class="formkit-field">
                    <input type="text" 
                        class="formkit-input" 
                        name="email_address" 
                        style= {{color:"#000", borderColor: "#e3e3e3", borderRadius:"4px", fontWeight:"400"}}
                        aria-label="Email Address" 
                        placeholder="Email Address" 
                        required=""/>
                </div>
            </div>
            <div class="picture"></div>
            <div class="Categories"></div>
            <div class="articles"></div>
            <div class="projects"></div>
            <div class="onlyfriends"></div>
        </div>
    </div>
);

export default Home;