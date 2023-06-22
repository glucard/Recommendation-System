import { useEffect, useState } from 'react'

function DialogBox() {


    const [bookName, setBookName] = useState("");
    const [recommendations, setRecommendations] = useState([]);

    const handleChange = (event) => {
        setBookName(event.target.value);
    }

    const handleSubmit = async (event) => {
        event.preventDefault();
        setRecommendations([])
        console.log(bookName);

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ input_book: bookName })
        };
        const response = await fetch('http://localhost:1080/predict', requestOptions);
        const data = await response.json();
        console.log(data)
        
        if(data['Prediction']) {
            setRecommendations(data['Prediction']);
        } else {
            setRecommendations(["Book title not found in database."])
        }
    }

    return (<>
        <form onSubmit={handleSubmit}>
            <label>
                Book Title: 
                <input type="text" name="name" onChange={handleChange} style={{lineHeight : 0, padding: 2.5, margin:10 }}/>
            </label>
            <input type="submit" value="Submit" style={{lineHeight : 0, padding: 2.5, margin:10 }}/>
        </form>
        {recommendations.length > 0 &&
        <h2>
          {recommendations.map((e, i) => <p key={i} style={{fontSize: 12, margin:0}}>{e}</p>)}
        </h2>
      }
    </>)
}

export default DialogBox;