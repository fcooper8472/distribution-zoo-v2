from utils import get_test_output_dir

from scipy.stats import norm
from scipy.stats import kstest

import numpy as np

import json


def load_params(dist_name: str) -> dict:
    params_file = get_test_output_dir() / dist_name / 'params.json'
    assert params_file.is_file()

    with open(params_file, 'r') as f:
        return json.load(f)


def test_validate_normal():

    test_params = load_params('normal')

    for fence in ['cpp', 'python']:

        pdf_file = get_test_output_dir() / 'normal' / fence / 'pdf.out'
        logpdf_file = get_test_output_dir() / 'normal' / fence / 'logpdf.out'
        rvs_file = get_test_output_dir() / 'normal' / fence / 'rvs.out'

        assert pdf_file.is_file()
        assert logpdf_file.is_file()
        assert rvs_file.is_file()

        pdf_data = np.loadtxt(pdf_file, delimiter=',')
        x = pdf_data[:, 0]
        y = pdf_data[:, 1]
        true_pdf = norm.pdf(x=x, loc=test_params['param_mean'], scale=test_params['param_std'])
        assert np.allclose(y, true_pdf)

        logpdf_data = np.loadtxt(logpdf_file, delimiter=',')
        x = logpdf_data[:, 0]
        y = logpdf_data[:, 1]
        true_pdf = norm.logpdf(x=x, loc=test_params['param_mean'], scale=test_params['param_std'])
        assert np.allclose(y, true_pdf)

        rvs_data = np.loadtxt(rvs_file)
        true_cdf = norm(loc=test_params['param_mean'], scale=test_params['param_std']).cdf
        ks_statistic, p_value = kstest(rvs_data, cdf=true_cdf)
        assert p_value > 0.05
