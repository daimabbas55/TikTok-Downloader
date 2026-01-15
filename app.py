from flask import Flask, render_template, request, jsonify, send_from_directory
import requests

app = Flask(__name__)

# Route for Home
@app.route('/')
def home():
    return render_template('index.html')

# Routes for Legal Pages
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml')

# API Route for Downloading
@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'success': False, 'message': 'Please provide a valid TikTok URL.'}), 400

    try:
        # Using tikwm.com API
        api_url = "https://www.tikwm.com/api/"
        # tikwm supports both GET and POST, POST is usually safer for long URLs
        response = requests.post(api_url, data={'url': url})
        result = response.json()

        if result.get('code') == 0:
            video_data = result.get('data')
            return jsonify({
                'success': True,
                'data': {
                    'title': video_data.get('title', 'No Title'),
                    'cover': video_data.get('cover'),
                    'play': video_data.get('play'),  # No watermark URL
                    'music': video_data.get('music'),
                    'author': video_data.get('author', {}).get('nickname', 'Unknown User')
                }
            })
        else:
            msg = result.get('msg', 'Unknown error occurred.')
            return jsonify({'success': False, 'message': f'Error: {msg}'}), 400

    except Exception as e:
        return jsonify({'success': False, 'message': f'Server Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
