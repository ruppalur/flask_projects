source : https://ron.sh/creating-real-time-charts-with-flask/
Objective:
 - Gather the facts
 - display in a chart
 - Learn about Server-Sent Events

Project scenario:
 - capture the memory utilization of device(my VM) using psutil and generator to publish the data
 - wrap the data into a json format
 - attach the timestamp
 - map it to a route
 - server will use SSE to send data to client using 'text/event-stream'
 - for chart using chart.js
 - in JS, use onmessage event, parse the json object published by server and update the chart realtime
 - for styling twitter bootstrap

Thanks to @roniemartinezz(twitter)
