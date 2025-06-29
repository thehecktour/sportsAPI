import React, { useEffect, useState } from 'react';

type Question = {
  question: string;
  options: string[];
  answer: string;
};

const Quiz = () => {
  const [questions, setQuestions] = useState<Question[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selected, setSelected] = useState<string | null>(null);
  const [showAnswer, setShowAnswer] = useState(false);

  useEffect(() => {
    fetch('/python.json')
      .then((res) => res.json())
      .then((data) => setQuestions(data));
  }, []);

  const current = questions[currentIndex];

  const handleSelect = (option: string) => {
    setSelected(option);
    setShowAnswer(true);
  };

  const nextQuestion = () => {
    setSelected(null);
    setShowAnswer(false);
    setCurrentIndex((prev) => (prev + 1) % questions.length);
  };

  if (!current) return <div className="loading">Loading...</div>;

  return (
    <div className="quiz-card">
      <h2>{current.question}</h2>
      <ul className="options">
        {current.options.map((opt) => (
          <li
            key={opt}
            className={`option ${
              showAnswer
                ? opt === current.answer
                  ? 'correct'
                  : opt === selected
                  ? 'wrong'
                  : ''
                : ''
            }`}
            onClick={() => !showAnswer && handleSelect(opt)}
          >
            {opt}
          </li>
        ))}
      </ul>
      {showAnswer && (
        <button onClick={nextQuestion} className="next-btn">
          Next
        </button>
      )}
    </div>
  );
};

export default Quiz;
