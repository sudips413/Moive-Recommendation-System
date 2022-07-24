import clustering
import os 

def clean_t_dataset():
    try:
        os.remove('Dataset_to_plot.csv')
    except:
        pass

def get_movie_name():
    input_movie = input("Enter the movie name: ").lower()
    movies = clustering.cluster_everything(input_movie)
    if type(movies) == int:
        pass
    else:
        print('---------------- Similar Movies ----------------')
        print(movies)

if __name__ == "__main__":
    get_movie_name()