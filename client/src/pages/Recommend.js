import React, { useEffect, useState } from 'react';
import Axios from 'axios';
import '../styles/App.css';
import { useHistory } from 'react-router-dom';

const Recommend = (props) => {
	const [result, setResult] = useState([]);
	https: useEffect(() => {
		Axios.post('http://127.0.0.1:5000/recommend', {
			id: props.location.state.id,
		}).then((res) => {
			setResult(res.data);
			console.log(res.data, 'result');
		});
	}, []);

	//Play/pause and playing only one audio at a time

	const history = useHistory();

	let currentAudio = new Audio();
	let isPlaying = false;
	let audio = new Audio();

	const playSong = (preview, id, index) => {
		audio.src = preview;

		if (!isPlaying) {
			isPlaying = true;
			audio.play();
			currentAudio.src = audio.src;
		} else {
			if (currentAudio.src === audio.src) {
				audio.pause();
				isPlaying = false;
			} else {
				audio.play();
				currentAudio.src = audio.src;
				isPlaying = true;
			}
		}
	};

	return (
		<div class="container">
			<div className="container">
				<div className="row">
					<button
						class="pulse"
						onClick={() => {
							history.goBack();
							audio.pause();
						}}
					>
						&larr; Back
					</button>
					<h3 className="heading-recommend">
						Song Recommendations for {props.location.state.song}{' '}
					</h3>
				</div>
			</div>
			{result && (
				<div className="container">
					<div className="row">
						{result.map((songs, index) => (
							<div
								className="col-lg-4 col-md-6 col-sm-6 col-sm-12"
								key={songs.spotify_id}
							>
								<div className="profile-card-2">
									<img
										src={songs.image_url}
										alt={songs.song_name}
										className="img img-responsive"
										onClick={() =>
											playSong(
												songs.preview,
												songs.spotify_id,
												index
											)
										}
									/>

									<div className="profile-name">
										{songs.song_name}
									</div>
									<div className="profile-username">
										{songs.artist_name}
									</div>
								</div>
							</div>
						))}
					</div>
				</div>
			)}
		</div>
	);
};

export default Recommend;
