require 'sinatra'
require 'json'

post '/predict' do
    content_type :json
    data = JSON.parse(request.body.read)
    text = data['text']

    # Call the Go model here (you can use system calls or HTTP requests)
    # For simplicity, let's assume the Go model is running on localhost:8080
    result = `./naive_bayes_model "#{text}"`
    
    { sentiment: result.strip }.to_json
end

# Run the Go model
`go run naive_bayes.go`