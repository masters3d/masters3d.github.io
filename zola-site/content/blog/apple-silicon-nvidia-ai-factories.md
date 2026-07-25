+++
title = "From Apple Silicon to NVIDIA AI Factories"
date = "2026-07-25"
description = "Revisiting a 2020 Apple Silicon and AR prediction in a world where NVIDIA, AI accelerators, software ecosystems, and electricity define the next computing platform."
template = "blog-post.html"
[taxonomies]
categories = ["AI & Tools"]
tags = ["ai", "nvidia", "apple", "apple-silicon", "spatial-computing", "hardware", "prediction", "retrospective"]
[extra]
editorial_track = "ai-and-tools"
+++

On June 21, 2020, I published
[Apple Chips == AR Glasses](/blog/apple-chips-ar-glasses/). I thought Apple's
rumored move away from Intel was bigger than a CPU swap. If Apple controlled the
CPU, GPU, Neural Engine, cameras, and operating system, it could build the next
computing platform without waiting for anybody else.

The timing still makes me smile. Apple
[announced its Mac transition to Apple Silicon](https://www.apple.com/newsroom/2020/06/apple-announces-mac-transition-to-apple-silicon/)
the next day.

Six years later, the interesting part is not simply whether the prediction was
right. Apple did replace Intel processors and AMD graphics across the Mac line.
Apple also built
[Vision Pro](https://www.apple.com/newsroom/2023/06/introducing-apple-vision-pro/),
which is almost exactly the device I described as something between a VR headset
and HoloLens. The interesting part is where I placed the center of gravity. I
thought the next platform would be on our faces. Instead, the largest change
happened in data centers, where NVIDIA chips train and run the models that are
changing how we use every other computer.

## What the Prediction Got Right

The central bet was vertical integration. A company that designs the chip,
software, and device can make trade-offs that are difficult when those parts
come from separate vendors. The M-series Mac proved that point. CPU, GPU,
memory, and Neural Engine became one system rather than a collection of
replaceable parts.

That integration did not make the Mac less powerful, as I worried it might. It
made the Mac more interesting. Unified memory became useful not only for
graphics but also for running models locally. The Neural Engine stopped looking
like a feature for a few phone tasks and started looking like an early signal of
where all personal computers were going.

The sensors were also a signal. Multiple cameras and LiDAR did become part of
Apple's spatial-computing system. Vision Pro uses cameras, eye tracking, hand
tracking, custom silicon, and software together. I got the shape of the machine
mostly right.

I got the use wrong. Vision Pro did not arrive as the Nintendo competitor I
imagined. Apple positioned it as a spatial computer, and its size and price made
it a very different product from a mass-market game console. AR glasses may
still become an everyday computer, but the difficult parts are now obvious:
battery, heat, weight, display quality, social acceptance, and a reason to wear
the device all day. A headset demonstration and a durable platform are not the
same thing.

## NVIDIA Moved the Center of Gravity

In 2020 I was looking at chips from the device inward. The AI boom forced me to
look from the data center outward.

NVIDIA did not win this position with a GPU alone. CUDA gave developers a
programming model. Libraries made common operations fast. Systems such as NVLink
and DGX connected accelerators into larger machines. Frameworks, cloud
providers, researchers, and companies built around that stack for years. By the
time large language models created enormous demand for parallel computation,
NVIDIA was selling a working system, not an isolated component.

The financial scale shows how quickly that system became infrastructure. For its
fiscal 2026, NVIDIA
[reported $215.9 billion in annual revenue](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026).
Its fourth-quarter data center revenue alone was $62.3 billion. Those numbers
are not just a story about chip sales. They show where the industry is spending
to create the next layer of computing.

Apple's integration is optimized around a person carrying or wearing a device.
NVIDIA's integration is optimized around racks of accelerators behaving like one
computer. Both strategies connect hardware and software tightly, but they
operate at different scales. Apple asks how much intelligence can fit within a
power and privacy budget on the device. NVIDIA asks how much computation can fit
within the networking, cooling, and power budget of a data center.

NVIDIA is not alone. Google has TPUs. Amazon has Trainium and Inferentia.
Microsoft has Maia. These companies are repeating the same lesson from Apple
Silicon: when a workload becomes important enough, designing the hardware and
software together becomes a strategic advantage. GPUs remain valuable because
models and methods are still changing quickly. Custom accelerators become
valuable when a company runs a large, predictable workload and can optimize the
whole path.

The competition is therefore larger than NVIDIA versus AMD. It is CUDA and a
broad ecosystem versus vertically integrated cloud systems, each with its own
chips, models, networks, and customers. NVIDIA has the strongest general
platform today. The cloud companies have scale, internal demand, and a reason to
reduce their dependence on any one supplier. Both can be true at once.

## The Computer Now Includes the Power Plant

The phrase "state of AI" can make this sound like a competition between models.
The models matter, but they sit inside a physical system. A model needs chips.
The chips need high-bandwidth memory and networking. The racks need cooling. The
data center needs land, transformers, and electricity.

The
[International Energy Agency estimates](https://www.iea.org/reports/energy-and-ai/executive-summary)
that global electricity demand from data centers will more than double by 2030
to about 945 terawatt-hours. That is a reminder that AI is not weightless
software. The constraint can move from model architecture to chip supply, then
to memory, networking, cooling, or the local electrical grid.

This also changes what "on-device AI" means. Local models can reduce latency,
protect private data, work without a network, and avoid paying a cloud inference
bill for every interaction. Cloud models can be much larger and can draw on
specialized infrastructure. The future is probably not one replacing the other.
It is a negotiated boundary. Devices will do the work that benefits from being
close to us, while data centers will do the work that benefits from enormous
shared computation.

That brings me back to glasses. The useful version of AR glasses may depend less
on putting a complete supercomputer on somebody's face and more on dividing the
work among sensors, a phone, local models, and cloud models. The glasses become
an interface to intelligence that lives across several computers. In that sense,
Apple chips may still lead to AR glasses, but NVIDIA and the rest of the AI
infrastructure world are part of the path too.

---

_The 2020 prediction taught me that the visible product is often downstream of a
less visible capability. I saw Apple's control of silicon and correctly expected
a new device, but I underestimated how much the next platform would depend on
data-center systems, software ecosystems, and power. The quest is no longer only
to put a computer on our faces. It is to decide what belongs on the device, what
belongs in the data center, and who controls the system connecting them._
