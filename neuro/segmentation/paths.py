from pathlib import Path

from neuro.atlas_tools import paths as reg_paths


class Paths:
    """
    A single class to hold all file paths that may be used. Any paths
    prefixed with "tmp__" refer to internal intermediate steps, and will be
    deleted if "--debug" is not used.
    """

    def __init__(self, registration_output_folder, downsampled_image):
        self.registration_output_folder = Path(registration_output_folder)
        self.downsampled_image = self.join(downsampled_image)

        self.tmp__inverse_transformed_image = self.join(
            "image_standard_space.nii"
        )
        self.tmp__inverse_transform_log_path = self.join(
            "inverse_transform_log.txt"
        )
        self.tmp__inverse_transform_error_path = self.join(
            "inverse_transform_error.txt"
        )

        self.annotations = self.join(reg_paths.ANNOTATIONS)
        self.hemispheres = self.join(reg_paths.HEMISPHERES)

        self.regions_directory = self.join("regions")
        self.region_summary_csv = self.regions_directory / "summary.csv"

        self.tracks_directory = self.join("tracks")
        self.track_points_file = self.tracks_directory / "points.h5"
        self.probe_summary_csv = self.tracks_directory / "summary.csv"

    def join(self, filename):
        return self.registration_output_folder / filename
