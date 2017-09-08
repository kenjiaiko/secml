#!/usr/bin/env python
# coding: utf-8

import numpy as np
import sys

class GaussianMixture(object):
	# reference: http://qiita.com/ctgk/items/22ce61fc0ffbc12c64d1
	def __init__(self, n_component):
		self.n_component = n_component
	
	def fit(self, X, iter_max=10):
		self.ndim = np.size(X, 1)
		self.weights = np.ones(self.n_component) / self.n_component
		self.means = np.random.uniform(X.min(), X.max(), (self.ndim, self.n_component))
		self.covs = np.repeat(10 * np.eye(self.ndim), self.n_component).reshape(self.ndim, self.ndim, self.n_component)
		for i in xrange(iter_max):
			params = np.hstack((self.weights.ravel(), self.means.ravel(), self.covs.ravel()))
			resps = self.expectation(X)
			self.maximization(X, resps)
			if np.allclose(params, np.hstack((self.weights.ravel(), self.means.ravel(), self.covs.ravel()))):
				break
		else:
			return -1
		return 0
	
	def gauss(self, X):
		diffs = X[:, :, None] - self.means
		precisions = np.linalg.inv(self.covs.T).T
		exponents = np.sum(np.einsum('nik,ijk->njk', diffs, precisions) * diffs, axis=1)
		return np.exp(-0.5 * exponents) / np.sqrt(np.linalg.det(self.covs.T).T * (2 * np.pi) ** self.ndim)
	
	def expectation(self, X):
		resps = self.weights * self.gauss(X)
		resps /=resps.sum(axis=-1, keepdims=True)
		return resps
	
	def maximization(self, X, resps):
		Nk = np.sum(resps, axis=0)
		self.weights = Nk / len(X)
		self.means = X.T.dot(resps) / Nk
		diffs = X[:, :, None] - self.means
		self.covs = np.einsum('nik,njk->ijk', diffs, diffs * np.expand_dims(resps, 1)) / Nk
	
	def predict_proba(self, X):
		gauss = self.weights * self.gauss(X)
		return np.sum(gauss, axis=-1)
	
	def classify(self, X):
		joint_prob = self.weights * self.gauss(X)
		return np.argmax(joint_prob, axis=1)

