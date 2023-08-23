import React from 'react';
import mentalHealthImage from './logo.png';
import './Main.css';
import Slider from "react-slick";
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";

function Main() {
  const [showMore, setShowMore] = React.useState(false);
  
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,          // Enable autoplay
    autoplaySpeed: 3000      // Change slide every 3 seconds
  };

  return (
    <div className="main-container">
      <div className="header-section">
        <img src={mentalHealthImage} alt="Mental Health" />
        <h1>Mental Health</h1>
      </div>
      <p>
        Mental health, often misconstrued as merely the absence of mental disorders, is a multifaceted concept that encompasses emotional, psychological, and social well-being. It plays a pivotal role in every phase of our lives, influencing how we think, feel, and act. Just as physical health is crucial for the optimal functioning of the body, mental health is indispensable for overall well-being and the ability to lead a balanced and productive life.
      </p>
      <p>
        At the core of mental health is emotional well-being. This pertains to how we handle stress, make decisions, and interact with others. Our emotional health can be influenced by factors such as genetics, brain chemistry, trauma, and life experiences. A strong emotional foundation allows us to build resilience against everyday challenges and recover from setbacks more effectively.
      </p>

      {showMore ? (
        <div className="more-info">
        <p>
            Psychological well-being, another facet of mental health, involves the ability to maintain a balanced state of mind. This balance is crucial for managing life's ups and downs, making sound decisions, and relating to others in constructive ways. Our psychological health is intertwined with our perception of self-worth, potential, and belonging.
        </p>
        <p>
            Social well-being, often overlooked, is equally vital. Humans are inherently social creatures, and our connections with others—be it family, friends, or the broader community—have a profound impact on our mental health. Positive social interactions can bolster feelings of love, connection, and belonging, acting as a buffer against mental health challenges.
        </p>
        <p>
            However, the path to achieving and maintaining good mental health isn't always straightforward. Life's inherent challenges, from personal hardships to global crises, can test our mental resilience. Factors such as genetic predispositions, traumatic events, and chronic physical illnesses can further complicate this journey. It's essential to recognize that seeking help during trying times is not a sign of weakness but rather an act of strength.
        </p>
        <p>
            Mental health disorders, ranging from anxiety and depression to more severe conditions like schizophrenia, have been stigmatized for centuries. This stigma, rooted in misunderstanding and prejudice, has often deterred individuals from seeking the help they need. However, as society becomes more informed, there's a growing understanding that mental health disorders are not a result of personal failures but are complex conditions interwoven with biological, psychological, and environmental factors.
        </p>
        <p>
            The importance of early intervention cannot be overstated. Recognizing the signs of mental health issues and seeking timely intervention can make a significant difference in outcomes. This is where awareness plays a pivotal role. By educating ourselves and others, we can create an environment where mental health is discussed openly, and individuals are encouraged to seek help without fear of judgment.
        </p>
        <p>
            In today's fast-paced world, where the lines between personal and professional lives often blur, it's more important than ever to prioritize mental well-being. Simple practices like mindfulness meditation, regular exercise, adequate sleep, and maintaining a balanced diet can go a long way in promoting mental health. Additionally, fostering strong personal relationships, seeking therapy, and, when necessary, medication can be instrumental in navigating the complexities of mental health.
        </p>
        <p>
            In conclusion, mental health is an integral aspect of our overall well-being, deserving as much attention, care, and understanding as physical health. As society progresses, it's our collective responsibility to destigmatize mental health issues, promote awareness, and create a world where everyone has access to the resources and support they need to thrive mentally. After all, a healthy mind is the cornerstone of a fulfilling life.
        </p>
        </div>
      ) : null}

      <button className="show-more-btn" onClick={() => setShowMore(!showMore)}>
        {showMore ? "Show Less" : "Show More"}
      </button>

      <div className="counselor-profile-container">
        <h2>Counselor Profile</h2>
        <Slider {...settings}>
          <div>
            <img src="/d1.png" alt="doctor 1" />
            <div className="slide-text">Counselor's biography. To be refined.</div>
          </div>
          <div>
            <img src="/d2.png" alt="doctor 2" />
            <div className="slide-text">Counselor's biography. To be refined.</div>
          </div>
          <div>
            <img src="/d3.png" alt="doctor 3" />
            <div className="slide-text">Counselor's biography. To be refined.</div>
          </div>
          <div>
            <img src="/d4.png" alt="doctor 4" />
            <div className="slide-text">Counselor's biography. To be refined.</div>
          </div>
          <div>
            <img src="/d5.png" alt="doctor 5" />
            <div className="slide-text">Counselor's biography. To be refined.</div>
          </div>
        </Slider>
      </div>
      
      <h2>Resources:</h2>
      <ul className="resource-list">
        <li><a href="https://foremind.com.au/" target="_blank" rel="noopener noreferrer">Foremind - Australia's #1 Worker Wellbeing Platform</a></li>
        <li><a href="https://www.who.int/health-topics/mental-health" target="_blank" rel="noopener noreferrer">World Health Organization: Mental Health</a></li>
        <li><a href="https://www.nimh.nih.gov/" target="_blank" rel="noopener noreferrer">National Institute of Mental Health</a></li>
        <li><a href="https://www.mayoclinic.org/diseases-conditions/mental-illness/symptoms-causes/syc-20374968" target="_blank" rel="noopener noreferrer">Mayo Clinic: Mental Illness</a></li>
      </ul>
    </div>
  );
}

export default Main;
