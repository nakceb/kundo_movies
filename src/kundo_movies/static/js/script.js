document.addEventListener('DOMContentLoaded', function() {
    // Handle movie details modal
    document.addEventListener('click', async function(e) {
        if (e.target.classList.contains('details-button')) {
            const title = e.target.dataset.title;
            const detailsDiv = document.getElementById('details-' + title);

            try {
                // Fetch movie details
                const response = await fetch(`/details/${title}`);
                const movieData = await response.json();

                // Details div for that movie
                detailsDiv.innerHTML = `
                    <div>
                        <h2>${movieData.Title} (${movieData.Year})</h2>
                        ${movieData.imdbRating !== "N/A"
                            ? `<div>IMDB rating:${movieData.imdbRating}/10</div>`
                            : ''}
                        ${movieData.Ratings
                            .filter(rating => rating.Source === "Rotten Tomatoes")
                            .map(rating => `<div>Rotten Tomatoes rating: ${rating.Value}</div>`)
                            .join('')}
                        <p>${movieData.Plot}</p>
                    </div>
                `;
            } catch (error) {
                detailsDiv.innerHTML = '<p>Error loading movie details</p>';
            }
        }
    });
});