# Efficient data structures and sampling of many light sources for Next Event Estimation
### Photon-based Next Event Estimation
Master's thesis - Andreas Mikolajewski - KIT Computer Graphics Group

#### Abstract

Modern photorealistic media production faces increasing computational ressource demands caused by an ever-expanding number of light sources to produce natural-looking images. A significant percentage of processing time goes towards casting shadow rays to calculate the direct lighting term with Next Event Estimation. As our evaluation shows, naively sampling many light sources in a path tracer quickly becomes impractical. We present a novel technique to importance sample many light sources called Photon-based Next Event Estimation (PNEE). In a preprocessing step,  similar to Photon Mapping, photons are scattered from all light sources into the scene. These photons are used to build cumulative distribution functions (CDF) that reflect the importance of the light sources to reduce the variance of the Monte Carlo integration. We evaluate multiple storage options and data structures for efficient lookups within the integrator. We introduce and utilize two novel data structures CDFs: sparse CDFs and interpolated CDFs. To mitigate variance edges and artifacts, we present several interpolation and approximation methods. We evaluate several variants of PNEE against naive NEE as well as PBRTs recent implementation, and demonstrate that even for moderately complex scenes a 50-100x speedup can be achieved.


