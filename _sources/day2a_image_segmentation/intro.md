# Image segmentation

This section contains an introdcution into image segmentation, a.k.a. pixel classification as well as creating meshes from segmented data. In particular, this will cover the following topics:

| Topic | Description | Link |
| ----- | ----------- | ---- |
| **Segmentation & Surfaces** | Introduction to image segmentation and surface extraction & processing | [Slides](Instance_segmentation.pf) |
| Thresholding | Basic technique to separate foreground from background | [Slides](https://github.com/BiAPoL/Image-data-science-with-Python-and-Napari-EPFL2022/raw/main/docs/day2d_image_segmentation/Thresholding.pdf) |
| Instance segmentation | Separating different objects in an image | [Slides](https://github.com/BiAPoL/Image-data-science-with-Python-and-Napari-EPFL2022/raw/main/docs/day2d_image_segmentation/Instance_segmentation.pdf)|
| Segmentation quality estimation | How to measure the quality of a segmentation | [Slides](https://github.com/BiAPoL/Image-data-science-with-Python-and-Napari-EPFL2022/raw/main/docs/day2d_image_segmentation/segmentation_quality_estimation.pdf)

The course will follow along the slides on **Segmentation & Surfaces**. The other slides are provided for reference and further explanations, if needed.

## Notebooks for exercise

In this session, make sure to execute the following notebooks:

- [Thresholding](./01_EXERCISE_Thresholding.ipynb)
- [Connected components](./09_connected_component_labeling.ipynb)
- [Voronoi otsu labelling](./11_voronoi_otsu_labeling.ipynb)
- [Marching cubes](./21_EXERCISE_marching_cubes.ipynb)

## Further information

Segmentation is a big topic. For further information, also check out the following topics and notebooks:

- [Morphological operations](https://github.com/BiAPoL/Quantitative_Bio_Image_Analysis_with_Python_2022/blob/main/docs/day2b_image_segmentation/03_Morphological_operations.ipynb)
- [Otsu thresholding](https://github.com/BiAPoL/Quantitative_Bio_Image_Analysis_with_Python_2022/blob/main/docs/day2b_image_segmentation/04_Otsu_threshold.ipynb)
- [Touching objects labelling](https://github.com/BiAPoL/Quantitative_Bio_Image_Analysis_with_Python_2022/blob/main/docs/day2c_instance_segmentation/10_touching_objects_labeling.ipynb)
- [Voronoi tesselation](https://github.com/BiAPoL/Quantitative_Bio_Image_Analysis_with_Python_2022/blob/main/docs/day2c_instance_segmentation/11_voronoi_tesselation.ipynb)
- [Segmentation in 3D](https://github.com/BiAPoL/Quantitative_Bio_Image_Analysis_with_Python_2022/blob/main/docs/day2c_instance_segmentation/12_Segmentation_3D.ipynb)
- [Segmenting membranes in 2D](https://github.com/BiAPoL/Quantitative_Bio_Image_Analysis_with_Python_2022/blob/main/docs/day2c_instance_segmentation/14_segmentation_2d_membranes.ipynb)
- [Seeded watershed](https://github.com/BiAPoL/Image-data-science-with-Python-and-Napari-EPFL2022/blob/main/docs/day2d_image_segmentation/15_EXERCISE_Seeded_watershed.md)
- [Removing labels at image edges](https://github.com/BiAPoL/Image-data-science-with-Python-and-Napari-EPFL2022/blob/main/docs/day2d_image_segmentation/15_remove_labels_on_image_edges.ipynb)
- [Morphological opening and closing](https://github.com/BiAPoL/Image-data-science-with-Python-and-Napari-EPFL2022/blob/main/docs/day2d_image_segmentation/16_open_close_labels.ipynb)
- [Segmentation metrics: The segmentation game](https://github.com/BiAPoL/Image-data-science-with-Python-and-Napari-EPFL2022/blob/main/docs/day2d_image_segmentation/19_the_segmentation_game.md)
- [Segmentation metrics: Estimate quality](https://github.com/BiAPoL/Image-data-science-with-Python-and-Napari-EPFL2022/blob/main/docs/day2d_image_segmentation/20_EXERCISE_Segmentation_quality_estimation.ipynb)