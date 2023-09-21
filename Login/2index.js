// Fetch data from API and update dashboard
fetch('api/dashboard')
  .then(response => response.json())
  .then(data => {
    document.querySelector('.dashboard-card:nth-child(1) .dashboard-data').textContent = data.calorieIntake;
    document.querySelector('.dashboard-card:nth-child(2) .dashboard-data').textContent = data.exerciseProgress;
    document.querySelector('.dashboard-card:nth-child(3) .dashboard-data').textContent = data.currentWeight;
  })
  .catch(error => console.error(error));