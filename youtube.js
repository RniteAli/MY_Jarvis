const { google } = require('googleapis');

// Create a new YouTube client
const youtube = google.youtube({
  version: 'v3',
  auth: 'AIzaSyB728nu_uNOhXfUCO_RJo6Cyg44QvbQU3Y',
});

// Function to search for videos
async function searchVideos(query) {
  try {
    const response = await youtube.search.list({
      part: 'snippet',
      q: query,
      type: 'video',
      maxResults: 5, // Adjust the number of results as needed
    });

    const videos = response.data.items;
    // Process the search results
    videos.forEach((video) => {
      console.log(`Title: ${video.snippet.title}`);
      console.log(`Channel: ${video.snippet.channelTitle}`);
      console.log(`Description: ${video.snippet.description}`);
      console.log('------------------------');
    });
  } catch (error) {
    console.error('Error searching for videos:', error);
  }
}

// Example usage
searchVideos('programming tutorials');
