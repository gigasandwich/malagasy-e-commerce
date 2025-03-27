import joblib
import extensions

def get_sentiments(comments: list):
    model_name = f'{extensions.trained_models_folder}/decisiontree-tfidf.pkl'.lower()
    model, vectorizer = load_model(f'./{model_name}')

    X_new = [comment.commentaire for comment in comments]
    X_new_vectorized = vectorizer.transform(X_new)
    y_new_predicted = model.predict(X_new_vectorized)

    for comment, sentiment in zip(comments, y_new_predicted):
        comment.sentiment = format_sentiment(sentiment)
    return comments

def format_sentiment(sentiment):
    return 'tsara' if sentiment == 1 else 'ratsy'

def load_model(model_path):
    try:
        loaded_data = joblib.load(model_path)
        return loaded_data['model'], loaded_data['vectorizer']
    except Exception as e:
        print(f"Error loading model: {e}")
        return None, None