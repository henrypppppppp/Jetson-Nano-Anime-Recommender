# Jetson-Nano-Anime-Recommender
This is an anime recommender. The user inserts an anime name(the capitalization matters) and this algorithm will recommend 10 similar anime. It makes use of chunks and sparse matrix to account for the Jetson Nano's limited memory.
![image](https://github.com/henrypppppppp/Jetson-Nano-Anime-Recommender/assets/138828516/7f55c684-e723-40aa-bb40-e3d3fa4cc1e3)
## The Algorithm
This algorithm utilizes collaborative filtering to recommend similar anime based on user ratings. It handles large datasets efficiently by processing data in chunks and uses a sparse matrix representation for memory optimization, given the Nano's limited space. The recommendations given depend on the anime the user puts in the line anime_id = anime[anime['name'] == 'Shingeki no Kyojin']['anime_id'].iloc[0]      . Shingeki no Kyojin, or Attack on Titan, is the anime input for that line, but can be changed as the user wishes.
## Running the Project
Make sure you have a Nvidia Jetson Nano. Running is self explanitory and not very hard. The program may take around 30 seconds or more to completely execute, so be patient.
As for libraries, make sure you have Nvidia Nano compatible versions of the following libraries:pandas, numpy, matplotlib, and scipy.
## The code
![image](https://github.com/henrypppppppp/Jetson-Nano-Anime-Recommender/assets/138828516/2cd9a446-96fd-46ab-90c3-30391054efc6)
