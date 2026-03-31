import * as React from 'react';
import Paper from '@mui/material/Paper';
import { styled } from '@mui/material/styles';
import { TagCloud } from 'react-tagcloud'

const colorOptions = {
  luminosity: 'dark',
  count: 27,
};

const WordPaper = styled(Paper)(({ theme }) => ({
    // width: 120,
    // height: 120,
    padding: theme.spacing(2),
    ...theme.typography.body2,
    textAlign: 'center',
  }));

export default function FloatingCloud({wall_id = "test", onClick=() => {}}) {
  const [words, setWords] = React.useState([]);

  React.useEffect(()=>{
    // Define API Getter
    const getWords = () => {
      // Call the API
      fetch(`/api/v1/words/${wall_id}`)
    .then(response => {
        if (!response.ok) {
          if (String(response.status) === "404") {
            window.location.href = "/";
            throw new Error("HTTP error " + response.status);
          }
        }
        return response.json();
    })
    .then(json => {
        setWords(json);
    })
    .catch(function () {
        console.error(`Failed to load words for ${wall_id}`)
    })
    }
    // Load Requisites when page Completes
    getWords();
    setInterval(getWords, 1000);
  },[wall_id]);



  return (
    <>
      <WordPaper variant="elevation" elevation={6} onClick={onClick}>
        <TagCloud
            minSize={20}
            maxSize={64}
            tags={words}
            colorOptions={colorOptions}
        />
      </WordPaper>
    </>
  )
}
